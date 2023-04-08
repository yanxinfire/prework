{{/*
Server Config
*/}}
{{- define "server.config" -}}
server_host: {{ .Values.server.server_host }}
server_port: {{ .Values.server.server_port }}
mysql_host: {{ .Values.mysqldb.mysql_host }}
mysql_password: {{ .Values.mysqldb.mysql_password }}
mysql_user: {{ .Values.mysqldb.mysql_user }}
mysql_port: {{ .Values.mysqldb.mysql_port }}
mysql_database: {{ .Values.mysqldb.mysql_database }}
{{ end }}
