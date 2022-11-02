import pusher

pusher_client = pusher.Pusher(
  app_id='1495958',
  key='e44bec1bf9ea6204f565',
  secret='eeec2f9e4ff678a0821a',
  cluster='mt1',
  ssl=True
)

pusher_client.trigger('my-channel', 'my-event', {'message': 'hello world'})
