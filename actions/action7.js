"use strict";
let datafire = require('datafire');

let twitter_labs = require('@datafire/twitter_labs').actions;
module.exports = new datafire.Action({
  id: "action7",
  handler: async (input, context) => {
    let result = await Promise.all([].map(item => twitter_labs.getOpenApiSpec({}, context)));
    return result;
  },
});
