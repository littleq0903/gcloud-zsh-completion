#compdef appcfg.py
#------------------------------------------------------------
# Description:
#
#  Completion script for App Engine appcfg.py script
#
# Author:
#
#  * Colin Su (https://github.com/littleq0903)
#
# Source Code:
#
#  https://github.com/littleq0903/gcloud-zsh-completion
#
#------------------------------------------------------------

## Utils

__get_yaml_files () {
    _wanted application expl 'Google App Engine Configuration' compadd $(command find . -depth 1 -name "*.yaml")
    _wanted application expl 'Google App Engine Configuration' compadd $(command echo '.')
}

## Actions
local -a _action_backends_arguments
_action_backends_arguments=(
	'configure:Reconfigure a backend without stopping it'
	'delete:Delete a backend'
	'list:List all backends configured for the app'
	'rollback:Roll back an update of a backend'
	'start:Start a backend'
	'stop:Stop a backend'
	'update:Update one or more backends'
)

local -a _action_arguments
_action_arguments=(
	'backends:Perform a backend action'

	'create_bulkloader_config:Create a bulkloader.yaml from a running application'
	'cron_info:Display information about cron jobs'
	'delete_version:Delete the specified version for an app'
	'download_app:Download a previously-uploaded app'
	'download_data:Download entities from datastore'
	'help:Print help for a specific action'
	'list_versions:List all uploaded versions for an app'
	'request_logs:Write request logs in Apache common log format'
	'resource_limits_info:Get the resource limits'
	'rollback:Rollback an in-progress update'
	'set_default_version:Set the default (serving) version'
	'start_module_version:Start a module version'
	'stop_module_version:Stop a module version'

	'update:Create or update an app version'
	'update_cron:Update application cron definitions'
	'update_dispatch:Update application dispatch definitions'
	'update_dos:Update application dos definitions'
	'update_indexes:Update application indexes'
	'update_queues:Update application task queue definitions'
	'upload_data:Upload data records to datastore'

	'vacuum_indexes:Delete unused indexes from application'
)

## Options
local -a _options_arguments
_options_arguments=(
  {-h,--help}'[Show the help message and exit]'
  {-q,--quiet}'[Print errors only]'
  {-v,--verbose}'[Print info level logs]'
  '--noisy[Print all logs]'
  {-s+,--server=}':The App Engine server:( )'
  {-e+,--email=}':The username to use. Will prompt if omitted:( )'
  {-H+,--host=}':Overrides the Host header sent with all RPCs:( )'
  '--no_cookies[Do not save authentication cookies to local disk]'
  '--skip_sdk_update_check Do not check for SDK updates'
  '--passin[Read the login password from stdin]'
  {-A+,--application=}':Set the application,overriding the application value from app.yaml file:( )'
  {-V+,--version=}':Set the (major) version,overriding the version value from app.yaml file:( )'
  {-r+,--runtime=}':Override runtime from app.yaml file:( )'
  {-E+,--env_variable=}':Set an environment variable,potentially overriding an env_variable value from app.yaml file (flag may be repeated to set multiple variables):( )'
  {-R,--allow_any_runtime}'[Do not validate the runtime in app.yam]'
  '--oauth2[Use OAuth2 instead of password auth]'
  '--oauth2_refresh_token=:An existing OAuth2 refresh token to use. Will not attempt interactive OAuth approval:( )'
  '--oauth2_access_token=:An existing OAuth2 access token to use. Will not attempt interactive OAuth approval:( )'
  '--authenticate_service_account[Authenticate using the default service account for the Google Compute Engine VM in which appcfg is being calle]'
  '--noauth_local_webserver[Do not run a local web server to handle redirects during OAuth authorization]'
  {-f,--force}'[Force deletion without being prompted]'
  '--has_header[Whether the first line of the input file should be skippe]'
  '--loader_opts= A string to pass to the Loader.initialize method'
  '--url=:The location of the remote_api endpoint:( )'
  '--batch_size=:jNumber of records to post in each request:( )'
  '--bandwidth_limit=:The maximum bytes/second bandwidth for transfers:( )'
  '--rps_limit=:The maximum records/second for transfers:( )'
  '--http_limit=:The maximum requests/second for transfers:( )'
  '--db_filename=:Name of the progress database file:( )'
  '--auth_domain=:The name of the authorization domain to use:( )'
  '--log_file=:File to write bulkloader logs.:If not supplied then a new log file will be created,named: bulkloader-log- TIMESTAMP:( )'
  '--dry_run[Do not execute any remote_api call]'
  '--namespace=:Namespace to use when accessing datastore:( )'
  '--num_threads=:Number of threads to transfer records with:( )'
  '--filename=:The name of the file where output data is to be written. (Required:( )'
  '--kind=:The kind of the entities to retrieve:( )'
  '--exporter_opts=:A string to pass to the Exporter.initialize method:( )'
  '--result_db_filename=:Database to write entities to for download:( )'
  '--config_file=:Name of the configuration file:( )'
  '--num_runs=:Number of runs of each cron job to displayDefault is :( )'
  '--no_precompilation:Disable automatic precompilation (ignored for Go apps)'
  '--backends[Update backends when performing appcfg update]'
  {-I+,--instance=}':Instance to debug:( )'
  {-n+,--num_days=}':Number of days worth of log data to get. The cut-off point is midnight US/Pacific. Use 0 to get all available logs. Default is 1,unless --append is also given; then the default is 0:( )'
  {-a,--append}'[Append to existing file]'
  '--severity=:Severity of app-level log messages to get. The range is 0 (DEBUG) through 4 (CRITICAL). If omitted,only request logs are returned:( )'
  '--vhost=:The virtual host of log messages to get. If omitted,all log messages are returned:( )'
  '--include_vhost[Include virtual host in log messages]'
  '--include_all[Include everything in log messages]'
  '--end_date=:End date (as YYYY-MM-DD) of period for log data. Defaults to today:( )'
)

## completion
local expl
local curcontext="$curcontext" state line
local -A opt_args

_arguments -C \
  $_options_arguments \
  ':action:->action' \
  '*::options:->options'

case $state in
  (action)
    _describe -t actions "Google App Engine appcfg.py Actions" _action_arguments
    ;;
  (options)
    local -a args

    case $words[1] in
      (backends)
        # if action argument is 'backends', give its subcommand
        _arguments -C \
          ':action:->action' \
          '*::options:->options'

        case $state in
          (action)
            _describe -t subactions "appcfg.py backends" _action_backends_arguments
            ;;
          (options)
            _arguments '*:feature:__get_yaml_files'
            ;;
        esac
        ;;
      (*)
        _arguments -C '*:feature:__get_yaml_files'
        ;;
    esac

    _arguments $args
    ;;
esac

return 0

# Local Variables:
# mode: Shell-Script
# sh-indentation: 2
# indent-tabs-mode: nil
# sh-basic-offset: 2
# End:
# vim: ft=zsh sw=2 ts=2 et
