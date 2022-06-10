
conf={
    'CONSUMER_KEY':'GVdEBJvZKR4bGnvFTv76Ooh3XniD5TQi',
    'CONSUMER_SECRET':'ugCADwJUOXUoiuuo'
}

live_base='https://api.safaricom.co.ke',
sandbox_base='https://sandbox.safaricom.co.ke'

urls={
    'live':{
      'auth':f'{live_base}/'
    },
    'sandbox':{
      'auth':f'{sandbox_base}/oauth/v1/generate?grant_type=client_credentials'
    }
}