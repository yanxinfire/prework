{{/*
Return the proper operator image name
*/}}
{{- define "api-server.image" -}}
{{- $registryName := (include "common.tplvalues.render" ( dict "value" .Values.image.registry "context" $)) -}}
{{- $repositoryName := (include "common.tplvalues.render" ( dict "value" .Values.image.repository "context" $)) -}}
{{- $imageName := .Values.image.name -}}
{{- $tag := .Values.image.tag | toString -}}

{{- printf "%s/%s/%s:%s" $registryName $repositoryName $imageName $tag -}}
{{- end -}}


{{/*
Common labels
*/}}
{{- define "security.operator.labels" -}}
app: {{ .Release.Name }}
chart: {{ include "common.names.chart" . }}
release: {{ .Release.Name }}
heritage: {{ .Release.Service }}
{{- end -}}
