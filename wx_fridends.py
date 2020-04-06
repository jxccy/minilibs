import frida, sys

def on_message(message, data):
    if message['type'] == 'send':
        print("[*] {0}".format(message['payload']))
    else:
        print(message)

#
# jscode = """
# Java.perform(function () {
#   // Function to hook is defined here
#   var MainActivity = Java.use('com.example.seccon2015.rock_paper_scissors.MainActivity');
#
#   // Whenever button is clicked
#   var onClick = MainActivity.onClick;
#   onClick.implementation = function (v) {
#     // Show a message to know that the function got called
#     send('onClick');
#
#     // Call the original onClick handler
#     onClick.call(this, v);
#
#     // Set our values after running the original onClick handler
#     this.m.value = 0;
#     this.n.value = 1;
#     this.cnt.value = 999;
#
#     // Log to the console that it's done, and we should have the flag!
#     console.log('Done:' + JSON.stringify(this.cnt));
#   };
# });
# """

jscode = '''
Java.perform(function () {
    var SnsUploadUI= Java.use('com.tencent.mm.plugin.sns.ui.SnsUploadUI');
    var ag = SnsUploadUI.ag.overload("android.os.Bundle");
    //get sns type
    ag.implementation=function(bundle){
    var ret = ag.call(this,bundle);
    send("sns type = " + this.tMY.value);
    return ret;
  };
});'''
#
# jscode = '''
# Java.perform(function () {
#     var ae = Java.use('com.tencent.mm.plugin.sns.ui.ae');
#     var ae_a = ae.a.overload("int","int","org.b.d.i","java.lang.String","java.util.List","com.tencent.mm.protocal.protobuf.bdi","java.util.LinkedList","int","boolean","java.util.List","com.tencent.mm.pointers.PInt","java.lang.String","int","int");
#     ae_a.implementation = function(isPrivate,syncFlag2,twitterAccessToken,desc,atList,location,list1,pasterLen,bool1,list2,pint1,str1,num1,num2){
#     var ret = ae_a.call(this,isPrivate,syncFlag2,twitterAccessToken,desc,atList,location,list1,pasterLen,bool1,list2,pint1,str1,num1,num2);
#     console.log("************Basic Info************");
#     console.log("isPrivate = " + isPrivate);
#     console.log("syncFlag2 = " + syncFlag2);
#     console.log("twitterAccessToken = " + twitterAccessToken);
#     console.log("desc = " + "'" + desc + "'");
#     if(atList.size()>0){
#         for(var i=0;i<atList.size();i++){
#             console.log("atList[" + i + "] = " + atList.get(0));
#         }
#     }
#     if(location != null){
#
#         if(location.yRD.value != null){
#             console.log("location.yRD = " + location.yRD.value);
#         }
#
#         if(location.yRE.value != null){
#             console.log("location.yRE = " + location.yRE.value);
#         }
#
#     }
#     console.log("list1 = " + list1);
#     console.log("pasterLen = " + pasterLen);
#     console.log("bool1 = " + bool1);
#     if(list2 != null){
#         console.log("list2 = " + list2.size());
#     }
#     else{
#         console.log("list2 = " + list2);
#     }
#     console.log("pint1 = " + pint1.value.value);
#     console.log("str1 = " + str1);
#     console.log("num1 = " + num1);
#
#     return ret;
# }//ae.a
#
# });'''


jscode = '''
Java.perform(function(){
        var ay_class = Java.use("com.tencent.mm.plugin.sns.model.ay");
        var desc = "{desc}"; 
        var ayInstance = ay_class.$new(2);
        ayInstance.adk(desc);
        ayInstance.commit();
    });
'''.format(desc="To be, or not to be, that is a question.")

process = frida.get_usb_device().attach('com.tencent.mm')

# process = frida.get_usb_device().attach('com.example.seccon2015.rock_paper_scissors')
script = process.create_script(jscode)
script.on('message', on_message)
print('[*] Running')
script.load()
sys.stdin.read()