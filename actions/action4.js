"use strict";
let datafire = require('datafire');

let fitbit = require('@datafire/fitbit').actions;
module.exports = new datafire.Action({
  id: "action4",
  handler: async (input, context) => {
    let result = await Promise.all([].map(item => fitbit.user._.foods.log.water.date.date.json.get({
      date: "",
    }, context)));
    return result;
  },
});
