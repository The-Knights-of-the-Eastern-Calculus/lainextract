from __future__ import print_function
import frida
import sys

def on_message(message, data):
    print("[%s] => %s" % (message, data))

def main(target_process):
    session = frida.attach(target_process)

    script = session.create_script("""

    // Find base address of current imported jvm.dll by main process fledge.exe
    var baseAddr = Module.findBaseAddress('lain_win.exe');
    console.log('lain_win.exe baseAddr: ' + baseAddr);

    var DecompressLZSS = resolveAddress('0x404810');

    Interceptor.attach(DecompressLZSS, {

        // When function is called, print out its parameters
        onEnter: function (args) {
            console.log('');
            console.log('[+] Called DecompressLZSS ' + DecompressLZSS);
            console.log('[+] compressed_data: ' + args[0]);
            console.log('[+] output_memory: ' + args[1]);
            console.log('[+] unknown_array: ' + args[2]);
            console.log('decompressed_length: ' + args[0].add(4).readU32())
     
            dumpAddr('Input', args[0], 1000);
            this.outptr = args[1];
            this.compressed_data = args[0];
            this.outsize = args[0].add(4).readU32();
        },

        // When function is finished
        onLeave: function (retval) {
            dumpAddr('Output', this.outptr, this.outsize, this.compressed_data); // Print out data array, which will contain de/encrypted data as output
            console.log('[+] Returned from DecompressLZSS: ' + retval.toInt32());
        }
    });
    
   /* Interceptor.attach(resolveAddress('0x404a00'), {

        // When function is called, print out its parameters
        onEnter: function (args) {
            console.log('');
            console.log('[+] Called FUN_00404a00');
            console.log('[+] param_1: ' + args[0]);
        },

        // When function is finished
        onLeave: function (retval) {
            console.log('[+] Returned from FUN_00404a00: ' + retval);
        }
    }); 
    
    Interceptor.attach(resolveAddress('0x404a20'), {

        // When function is called, print out its parameters
        onEnter: function (args) {
            console.log('');
            console.log('[+] Called FUN_00404a20');
            console.log('[+] param_1: ' + args[0]);
        },

        // When function is finished
        onLeave: function (retval) {
            console.log('[+] Returned from FUN_00404a20: ' + retval);
        }
    });
    
    Interceptor.attach(resolveAddress('0x404ac0'), {

        // When function is called, print out its parameters
        onEnter: function (args) {
            console.log('');
            console.log('[+] Called FUN_00404ac0');
            console.log('[+] param_1: ' + args[0]);
        },

        // When function is finished
        onLeave: function (retval) {
            console.log('[+] Returned from FUN_00404ac0: ' + retval);
        }
    });
    
    Interceptor.attach(resolveAddress('0x404a40'), {

        // When function is called, print out its parameters
        onEnter: function (args) {
            console.log('');
            console.log('[+] Called FUN_00404a40');
            console.log('[+] param_1: ' + args[0]);
        },

        // When function is finished
        onLeave: function (retval) {
            console.log('[+] Returned from FUN_00404a40: ' + retval);
        }
    });

    Interceptor.attach(resolveAddress('0x404ae0'), {

        // When function is called, print out its parameters
        onEnter: function (args) {
            console.log('');
            console.log('[+] Called FUN_00404ae0');
            console.log('[+] param_1: ' + args[0]);
        },

        // When function is finished
        onLeave: function (retval) {
            console.log('[+] Returned from FUN_00404ae0: ' + retval);
        }
    }); */

    function dumpAddr(info, addr, size, compressed_data) {
        if (addr.isNull())
            return;
        console.log('compressed_data: ' + compressed_data);
        var buf = addr.readByteArray(size);
        if (compressed_data != undefined) {
            console.log('C:\\\\Users\\\\User\\\\Pictures\\\\lain_bootleg_decompressed\\\\' + compressed_data + '_decompressed.bmp');
            var file = new File('C:\\\\Users\\\\User\\\\Pictures\\\\lain_bootleg_decompressed\\\\' + compressed_data + '_decompressed.bmp', 'wb');
            file.write(buf);
            file.close()
        }
        if (size > 1500) { console.log('decompressed size > 1500');return;}

        console.log('Data dump ' + info + ' :');
        

        // If you want color magic, set ansi to true
        console.log(hexdump(buf, { offset: 0, length: size, header: true, ansi: false }));
    }

    function resolveAddress(addr) {
        var idaBase = ptr('0x400000'); // Enter the base address of jvm.dll as seen in your favorite disassembler (here IDA)
        var offset = ptr(addr).sub(idaBase); // Calculate offset in memory from base address in IDA database
        var result = baseAddr.add(offset); // Add current memory base address to offset of function to monitor
        console.log('[+] New addr=' + result); // Write location of function in memory to console
        return result;
    }
""")
    script.on('message', on_message)
    script.load()
    print("[!] Ctrl+D on UNIX, Ctrl+Z on Windows/cmd.exe to detach from instrumented program.\n\n")
    sys.stdin.read()
    session.detach()

if __name__ == '__main__':
    if len(sys.argv) != 2:
        print("Usage: %s <process name or PID>" % __file__)
        sys.exit(1)

    try:
        target_process = int(sys.argv[1])
    except ValueError:
        target_process = sys.argv[1]
    main(target_process)
