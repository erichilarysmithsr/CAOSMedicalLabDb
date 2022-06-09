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

{% code title="caos.html" %}
```html
<html>
  <head>
   <link rel="stylesheet" href="https://pyscript.net/alpha/pyscript.css" />
   <script defer src="https://pyscript.net/alpha/pyscript.js"></script>
  <\head>
    <body>
      <py-script>
      
       patients = 'p'
       
       patients_name = 'African American'
       patients_name1 = 'Latino American'
       patients_name2 = 'Asian American'
       patients_name3 = 'Native American'
       patients_name4 = 'Mideastern American'
       patients_name5 = 'White American'
       
       African_American = 'a'
       Latino_American = 'l'
       Asian_American = 's'
       Native_American = 'n'
       Mideastern_American = 'm'
       White_American = 'w'
       
       a + l + s + n + m + w = p
       
       print(a + 1 + s + n + m + w)
       
      <\py-script>
     <\body>
 <\html>

```
{% endcode %}

{% code title="main.js" %}
```javascript
// let url = 'https://api.sheety.co/2038ea59d35e3cf806679a2706330dc9/replicatedPimaIndiansDatasetForDiabetes/formResponses1';fetch(url).then((response) => response.json()).then(json => {  // Do something with the data  console.log(json.formResponses1S);});

```
{% endcode %}

{% swagger method="post" path="" baseUrl="https://api.sheety.co/2038ea59d35e3cf806679a2706330dc9/replicatedPimaIndiansDatasetForDiabetes/formResponses1" summary="Form Response 1b" %}
{% swagger-description %}
Update a Row
{% endswagger-description %}

{% swagger-response status="200: OK" description="HTTP OK" %}
```javascript
<{
    // Response
}
```
{% endswagger-response %}

{% swagger-response status="404: Not Found" description="Page Not Found" %}
```javascript
{
    // Response
}
```
{% endswagger-response %}
{% endswagger %}

{% code title="main.js" %}
```javascript
// let url = 'https://api.sheety.co/2038ea59d35e3cf806679a2706330dc9/replicatedPimaIndiansDatasetForDiabetes/formResponses1';
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
{% endcode %}

{% swagger src=".gitbook/assets/Math4YouByUsGroupIL-CAOS-1.0.0-resolved.yaml" path="undefined" method="undefined" %}
[Math4YouByUsGroupIL-CAOS-1.0.0-resolved.yaml](.gitbook/assets/Math4YouByUsGroupIL-CAOS-1.0.0-resolved.yaml)
{% endswagger %}

{% swagger src=".gitbook/assets/metabis.yaml" path="undefined" method="undefined" %}
[metabis.yaml](.gitbook/assets/metabis.yaml)
{% endswagger %}
