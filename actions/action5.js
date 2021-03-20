"use strict";
let datafire = require('datafire');

let google_sheets = require('@datafire/google_sheets').actions;
module.exports = new datafire.Action({
  id: "action5",
  handler: async (input, context) => {
    let spreadsheet = await Promise.all([].map(item => google_sheets.sheets.spreadsheets.get({
      spreadsheetId: "",
      includeGridData: true,
      ranges: [],
      access_token: "",
      callback: "",
      fields: "",
      key: "",
      oauth_token: "",
      prettyPrint: true,
    }, context)));
    return spreadsheet;
  },
});
