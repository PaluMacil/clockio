from . import *
# import ssl

# context = ssl.SSLContext(ssl.PROTOCOL_TLSv1_2)
# context.load_cert_chain('danwolf.net.crt', 'danwolf.net.key')
application = create_app()

if __name__ == '__main__':
    application.run(host='0.0.0.0', port=8000)
