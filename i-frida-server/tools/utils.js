    //查看java堆栈
    function showStacks() {
        Java.perform(function(){
            var log = Java.use("android.util.Log");
            var exception = Java.use("java.lang.Exception").$new();
            send(log.getStackTraceString(exception));
        });
    }

    //string.getBytes
    function getBytes(chrList) {
        var bytes = [];
            for (var i = 0; i < chrList.length; i++) {
                bytes.push(chrList.charCodeAt(i));
            }
        return bytes;
    }

    //将字节数组转成十六进制形式字符串
    function bytesToHex(arr) {
        var str = '';
        var k,j;
        for(var i = 0; i<arr.length; i++) {
        k = arr[i];
        j = k;
        if (k < 0) {
        j = k + 256;
        }
        if (j < 16) {
        str += "0";
        }
        str += j.toString(16);
        }
        return str;
    };

    //将字符串转16byte
	function stringToBytes(str) {
        var ch, st, re = [];
        for (var i = 0; i < str.length; i++ ) {
            ch = str.charCodeAt(i);
            st = [];

           do {
                st.push( ch & 0xFF );
                ch = ch >> 8;
            }
            while ( ch );
            re = re.concat( st.reverse() );
        }
        return re;
    }

    //十六进进制字符串转byte数组
    function hexToBytes(str) {
		var pos = 0;
		var len = str.length;
		if (len % 2 != 0) {
			return null;
		}
		len /= 2;
		var hexA = new Array();
		for (var i = 0; i < len; i++) {
			var s = str.substr(pos, 2);
			var v = parseInt(s, 16);
			hexA.push(v);
			pos += 2;
		}
		return hexA;
    }

    //字符串转 十六进进制 字符串
    function stringToHex(str) {
		var val = "";
		for (var i = 0; i < str.length; i++) {
			if (val == "")
				val = str.charCodeAt(i).toString(16);
			else
				val += str.charCodeAt(i).toString(16);
		}
		return val;
    }