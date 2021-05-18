import pusher

pusher_client = pusher.Pusher(
  app_id='1153073',
  key='6428ed518ffd621af0c7',
  secret='9b59992275496f8bf1be',
  cluster='mt1',
  ssl=True
)

pusher_client.trigger('my-channel', 'my-event', {'message': 'hello world'})
