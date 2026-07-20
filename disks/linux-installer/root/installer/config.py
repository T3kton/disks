import os
import shlex
import configparser
from io import StringIO
from configparser import NoOptionError
from installer.procutils import chroot_execute
from libconfig.libconfig import Config
from libconfig.jinja2 import FileSystemLoader, Environment

config = None
template = None

config_values = { '_installer': {} }


def initConfig( install_root, template_path, profile_path, contractor ):
  global config, template

  config = Config( contractor, template_path, ':memory:', install_root )
  config.updateCacheFromContractor()

  env = Environment( loader=FileSystemLoader( os.path.dirname( profile_path ) ) )
  template = env.get_template( os.path.basename( profile_path ) )


def getValues():
  return config.getValues()


def getProfile():
  values = config.getValues()
  configfp = StringIO( template.render( values ) )
  profile = configparser.RawConfigParser()
  try:
    profile.read_file( configfp )

  except configparser.Error as e:
    raise Exception( 'Error Parsing distro profile: "{0}"'.format( e ) )

  return profile


def writeShellHelper():
  with open( '/target/config_data', 'w' ) as config_data:
    values = config.getValues()
    for value in values:
      config_data.write( '{0}=\'{1}\'\n'.format( value, shlex.quote( str( values[ value ] ) ) ) )


def updateConfig( category, newvals ):
  global config_values
  config_values[ '_installer' ][ category ] = newvals

  config.setOverlayValues( config_values )


def renderTemplates( template_list ):
  print( 'Rendering templates "{0}"...'.format( ','.join( template_list ) ) )
  template_list = [ i.strip() for i in template_list ]
  config.configPackage( '', template_list, True, False, True, True )


def baseConfig( profile ):
  renderTemplates( profile.get( 'config', 'base_templates' ).split( ',' ) )
  try:
    chroot_execute( profile.get( 'config', 'base_cmd' ) )
  except NoOptionError:
    pass


def fullConfig():
  template_list = config.getTemplateList( '' )
  renderTemplates( template_list )
