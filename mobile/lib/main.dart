import 'package:flutter/material.dart';
import 'package:webview_flutter/webview_flutter.dart';

void main() {
  runApp(MyApp());
}

class MyApp extends StatelessWidget {
  // This widget is the root of your application.
  @override
  Widget build(BuildContext context) {
    return MaterialApp(
      title: 'Barter App',
      theme: ThemeData(
        primarySwatch: Colors.blue,
        visualDensity: VisualDensity.adaptivePlatformDensity,
      ),
      home: WebViewExample(),
    );
  }
}

class WebViewExample extends StatefulWidget {
  @override
  WebViewExampleState createState() => WebViewExampleState();
}

class WebViewExampleState extends State<WebViewExample> {
  @override
  void initState() {
    super.initState();
  }

  @override
  Widget build(BuildContext context) {
    return FutureBuilder(
      future: DefaultAssetBundle.of(context)
          .loadString('assets/webapp/index.html'), // async work
      builder: (BuildContext context, AsyncSnapshot<String> snapshot) {
        switch (snapshot.connectionState) {
          case ConnectionState.waiting:
            return Text('Loading....');
          default:
            if (snapshot.hasError)
              return Text('Error: ${snapshot.error}');
            else {
              // final String contentBase64 = base64Encode(const Utf8Encoder().convert(snapshot.data));
              //               return WebView(initialUrl: 'data:text/html;base64,$contentBase64', javascriptMode: JavascriptMode.unrestricted);
              return WebView(
                  initialUrl: 'http://10.0.2.2:8080',
                  javascriptMode: JavascriptMode.unrestricted);
            }
        }
      },
    );
  }
}
