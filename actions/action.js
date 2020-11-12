"use strict";
let datafire = require('datafire');

let healthcare_gov = require('@datafire/healthcare_gov').actions;
module.exports = new datafire.Action({
  handler: async (input, context) => {
    let articlesList = await Promise.all([].map(item => healthcare_gov.api.articlesmediaTypeExtension.get({
      mediaTypeExtension: ".json",
    }, context)));
    return articlesList;
  },
});
