rpc.exports =
    {
        getmas: function (i, str, strArr, str2) {
            var result = "";
            Java.perform(function () {
                var UserInfo = Java.use("com.ss.android.common.applog.UserInfo");
                var cssca = Java.use("com.ss.sys.ces.a");
                var eagleEye = Java.use("com.ss.android.common.applog.EagleEye");

                var str = UserInfo.getUserInfo(
                    Number(i),
                    "" + str,
                    ("" + strArr).split(","),
                    "" + str2);
                var as = str.substr(0, 22);
                var cp = str.substr(22, str.length);
                var mas = eagleEye.byteArrayToHexStr(cssca.encode(getBytes(as)));
                result = "&as=" + as + "&cp=" + cp + "&mas=" + mas;
            });
            return result;
        }
}