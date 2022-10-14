// Import:
using PostmarkDotNet;

// Send an email asynchronously:
var message = new PostmarkMessage()
{
  To = "erichilarysmith@outlook.com",
  From = "support@ericyellowscreencomputers.com",
  TrackOpens = true,
  Subject = "A complex email",
  TextBody = "Hello dear Postmark user.",
  HtmlBody = "<strong>Hello</strong> dear Postmark user. <img src="cid:embed_name.jpg"/>",
  MessageStream = "outbound",
  Tag = "New Year's Email Campaign",
  Headers = new HeaderCollection{
    {"X-CUSTOM-HEADER", "Header content"}
  }
};

var imageContent = File.ReadAllBytes("test.jpg");
message.AddAttachment(imageContent, "test.jpg", "image/jpg", "cid:embed_name.jpg");

var client = new PostmarkClient("423ee822-bee9-4974-8234-1d095e65be2e");
var sendResult = await client.SendMessageAsync(message);

if (sendResult.Status == PostmarkStatus.Success){ /* Handle success */ }
else { /* Resolve issue.*/ }
