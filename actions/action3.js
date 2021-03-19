"use strict";
let datafire = require('datafire');

let chompthis = require('@datafire/chompthis').actions;
module.exports = new datafire.Action({
  id: "action3",
  handler: async (input, context) => {
    let brandedFoodObject = await Promise.all([].map(item => chompthis.food.branded.barcode.php.get({
      code: "",
    }, context)));
    return brandedFoodObject;
  },
});
