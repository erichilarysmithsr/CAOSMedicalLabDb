"use strict";
let datafire = require('datafire');

let c19qrserver_local = require('@datafire/c19qrserver_local').actions;
module.exports = new datafire.Action({
  id: "action6",
  handler: async (input, context) => {
    let result = await Promise.all([].map(item => c19qrserver_local.users.get({}, context)));
    return result;
  },
});
