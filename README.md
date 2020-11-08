# CAOS Medical Lab API

{% api-method method="post" host="https://api.postmarkapp.com" path="/message-streams" %}
{% api-method-summary %}
IMHOTEP Bizarros message-streams
{% endapi-method-summary %}

{% api-method-description %}

{% endapi-method-description %}

{% api-method-spec %}
{% api-method-request %}
{% api-method-path-parameters %}
{% api-method-parameter name="MessageStreamType" type="string" required=false %}
Broadcasts Transactional
{% endapi-method-parameter %}
{% endapi-method-path-parameters %}
{% endapi-method-request %}

{% api-method-response %}
{% api-method-response-example httpCode=200 %}
{% api-method-response-example-description %}

{% endapi-method-response-example-description %}

```

```
{% endapi-method-response-example %}
{% endapi-method-response %}
{% endapi-method-spec %}
{% endapi-method %}

{% api-method method="get" host="https://api.caosreaxson.com" path="/v1/medicalobjects/:stream\_id" %}
{% api-method-summary %}
Get Sifidious message-streams
{% endapi-method-summary %}

{% api-method-description %}
This endpoint allows you to get medical objects.
{% endapi-method-description %}

{% api-method-spec %}
{% api-method-request %}
{% api-method-path-parameters %}
{% api-method-parameter name="stream\_id" type="string" %}
projectID of the medical object to get, for the health api.
{% endapi-method-parameter %}
{% endapi-method-path-parameters %}

{% api-method-headers %}
{% api-method-parameter name="Authentication" type="string" required=false %}
Authentication token to track down who can use the health api.
{% endapi-method-parameter %}
{% endapi-method-headers %}

{% api-method-query-parameters %}
{% api-method-parameter name="GoogleFit" type="array" %}
The API will do its best to find a medical object matching the patient health information.
{% endapi-method-parameter %}

{% api-method-parameter name="Fitbit" type="array" %}
Whether the Patient Walking    Speed should be high or low..
{% endapi-method-parameter %}
{% endapi-method-query-parameters %}
{% endapi-method-request %}

{% api-method-response %}
{% api-method-response-example httpCode=200 %}
{% api-method-response-example-description %}
Medical Objects successfully retrieved.
{% endapi-method-response-example-description %}

```
{    "name": "Medical Objects",    "items": "grocery_list",    "food": "McData"}
```
{% endapi-method-response-example %}

{% api-method-response-example httpCode=404 %}
{% api-method-response-example-description %}
Could not find a cake matching this query.
{% endapi-method-response-example-description %}

```
{    "message": "Ain't no cake like that."}
```
{% endapi-method-response-example %}
{% endapi-method-response %}
{% endapi-method-spec %}
{% endapi-method %}



