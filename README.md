# REST Digester

Automagically generate docs for apps' closed REST APIs 

## Getting started

1. Install the certificate on your phone __(see below)__
2. Connect your phone and computer to the same wifi network (I was able to do this on secured school wifi, so it'll probably work for you)
3. Get your computer's IP address to proxy through. On Mac, it's on System Preferences > Network. Look for: "Wi-Fi is connected to NetworkName and has the IP address XXX.YY.XXX.XXX."
4. On your iPhone, go to Settings > Wifi > tap on connected network > switch HTTP Proxy to Manual. Set the server to the above IP address (__XXX.YY.XXX.XXX__) and the port to __8080__.
5. Everything should be good to go now!
4. `mitmproxy -w output.out`
5. Start using the app you want to reverse.
6. Find the relevant API endpoint and run it again with `mitmdump -w output.out "~d api\.zondr\.com"`

## Installing the cert

1. `pip install mitmproxy`
2. Run `mitmproxy` to generate the certificate locally.
2. Email `~/.mitmproxy/mitmproxy-ca-cert.pem` to yourself
3. Open the attachment in the __official Mail app__ (not a third-party email client) on your phone and install it.

It should also be possible to do this with [mitm.it](http://mitm.it).

If you run into any issues running mitmproxy, [this page](https://github.com/dutzi/tamper/wiki/Troubleshooting) lists some common errors and solutions.

## Useful programs
 - [Squidman](http://squidman.net/squidman/)
 - Charles ([configuration](http://stackoverflow.com/a/11661124))

## Generate blueprint docs
https://github.com/apiaryio/curl-trace-parser

## Resources
 * [Reversing the Kayak app](http://www.shubhro.com/2014/12/18/reverse-engineering-kayak-mitmproxy/)
 * [Faking an app that receives requests](https://github.com/mitmproxy/mitmproxy/blob/master/examples/proxapp.py)
 * [Bootstrap snippet](http://bootsnipp.com/snippets/featured/panel-table-with-filters-per-column)
