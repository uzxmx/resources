// let printBuffer1_addr = DebugSymbol.fromName('Buffer::GetLen() const').address;
// DebugSymbol.getFunctionByName('Buffer::GetLen() const')
// console.log(printBuffer1_addr);

let moduleUtils = require('/Users/xmx/.pwn/frida/lib/module.js');

let symbol1 = moduleUtils.findModuleSymbol('main', '_Z11printBufferP6Buffer');
let symbol2 = moduleUtils.findModuleSymbol('main', '_Z11printBufferR6Buffer');
let addr = moduleUtils.findModuleSymbol('main', '_ZNK6Buffer6GetLenEv').address;
let getlen = new NativeFunction(addr, 'uint64', ['pointer']);


// let Comm_SKBuffer_GetLen_addr = DebugSymbol.fromName('Comm::SKBuffer::GetLen() const').address;
// console.log('Comm_SKBuffer_GetLen_addr', Comm_SKBuffer_GetLen_addr);
// let Comm_SKBuffer_GetLen_func = new NativeFunction(Comm_SKBuffer_GetLen_addr, 'uint64', ['pointer']);
// 
Interceptor.attach(symbol2.address, {
  onEnter: function(args) {
    console.log(getlen(this.context.rdi));
  }
});
