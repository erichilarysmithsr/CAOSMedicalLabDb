"use strict";
let datafire = require('datafire');

let google_fitness = require('@datafire/google_fitness').actions;
module.exports = new datafire.Action({
  handler: async (input, context) => {
    let result = await Promise.all([].map(item => google_fitness.oauthCallback({
      code: "",
    }, context)));
    return result;
  },
});
