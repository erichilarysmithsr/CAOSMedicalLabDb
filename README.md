---
description: The Hub for Pharmakon Health Cloud
---

# ♿ CAOS API

### COMET FISH UI Functions

{% swagger method="get" path="" baseUrl="https://api.sheety.co/2038ea59d35e3cf806679a2706330dc9/replicatedPimaIndiansDatasetForDiabetes/formResponses1" summary="Form Response 1" %}
{% swagger-description %}
Retrieve rows from your sheet
{% endswagger-description %}

{% swagger-response status="200: OK" description="HTTP OK" %}
```javascript
{
    // Response
}
```
{% endswagger-response %}

{% swagger-response status="404: Not Found" description="HTTP Status Code" %}
```javascript
{
    // Response
}
```
{% endswagger-response %}
{% endswagger %}

```javascript
/ let url = 'https://api.sheety.co/2038ea59d35e3cf806679a2706330dc9/replicatedPimaIndiansDatasetForDiabetes/formResponses1';
  let body = {
    formResponses1: {
      ...
    }
  }
  fetch(url, {
    method: 'POST',
    body: JSON.stringify(body)
  })
  .then((response) => response.json())
  .then(json => {
    // Do something with object
    console.log(json.formResponses1);
  });
```
