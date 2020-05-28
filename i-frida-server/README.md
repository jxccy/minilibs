# i-frida-server
目录

0x1.什么是Flask框架

0x2.i-frida-server


 0x0
   这套框架是我前段时间工作中开发的,当时逆某音的时候存在ollvm混淆,实在干不过,没办法这才想到利用frida来hook完成算法的调用,但是利用fridahook只有本机器可以调用,其他同事没法调用,后来想到利用friida rpc+flask框架暴露其API接口,可直接通过ip地址接口访问调用算法.


 0x1
    Flask是一个轻量级的可定制框架，使用Python语言编写，较其他同类型框架更为灵活、轻便、安全且容易上手。它可以很好地结合MVC模式进行开发，开发人员分工合作，小型团队在短时间内就可以完成功能丰富的中小型网站或Web服务的实现。另外，Flask还有很强的定制性，用户可以根据自己的需求来添加相应的功能，在保持核心功能简单的同时实现功能的丰富与扩展，其强大的插件库可以让用户实现个性化的网站定制，开发出功能强大的网站。引用https://baike.baidu.com/item/Flask/1241509?fr=aladdin


  0x2
   它是一个基于fridaRpc和Flask框架的一个组合框架,大大方便了其他客户端调用,对fridahook进行了分装和整合,降低了他们之间的耦合度,
   项目启动之后:
   然后就可以通过127.0.0.1:5001/xx访问接口


开启项目

 * Serving Flask app "run" (lazy loading)
 * Environment: production
   WARNING: This is a development server. Do not use it in a production deployment.
   Use a production WSGI server instead.
 * Debug mode: off
 * Running on http://0.0.0.0:5001/ (Press CTRL+C to quit)


   ps:
             仅供学习使用,其他后果本人一概不负责
             最后 github 地址    https://github.com/iio97/i-frida-server
             看雪帖子:https://bbs.pediy.com/thread-255460.htm
