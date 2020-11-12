"use strict";
let datafire = require('datafire');

let fitbit = require('@datafire/fitbit').actions;
module.exports = new datafire.Action({
  handler: async (input, context) => {
    let result = await Promise.all([].map(item => fitbit.oauthCallback({
      code: "",
    }, context)));
    return result;
  },
});
