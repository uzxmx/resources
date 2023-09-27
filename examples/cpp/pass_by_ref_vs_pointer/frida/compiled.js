(function(){function r(e,n,t){function o(i,f){if(!n[i]){if(!e[i]){var c="function"==typeof require&&require;if(!f&&c)return c(i,!0);if(u)return u(i,!0);var a=new Error("Cannot find module '"+i+"'");throw a.code="MODULE_NOT_FOUND",a}var p=n[i]={exports:{}};e[i][0].call(p.exports,function(r){var n=e[i][1][r];return o(n||r)},p,p.exports,r,e,n,t)}return n[i].exports}for(var u="function"==typeof require&&require,i=0;i<t.length;i++)o(t[i]);return o}return r})()({1:[function(require,module,exports){
function findModuleSymbol(moduleName, symbolName) {
  return Module.enumerateSymbols(moduleName)
    .find(function(e) {
      return symbolName === e.name;
    });
}

module.exports = {
  findModuleSymbol: findModuleSymbol,
};

},{}],2:[function(require,module,exports){
// let printBuffer1_addr = DebugSymbol.fromName('Buffer::GetLen() const').address;
// DebugSymbol.getFunctionByName('Buffer::GetLen() const')
// console.log(printBuffer1_addr);
// 

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

},{"/Users/xmx/.pwn/frida/lib/module.js":1}]},{},[2])
//# sourceMappingURL=data:application/json;charset=utf-8;base64,eyJ2ZXJzaW9uIjozLCJzb3VyY2VzIjpbIi4uLy4uLy4uLy4uLy4uLy5hc2RmL2luc3RhbGxzL25vZGVqcy8xMi4xMy4wLy5ucG0vbGliL25vZGVfbW9kdWxlcy9mcmlkYS1jb21waWxlL25vZGVfbW9kdWxlcy9icm93c2VyLXBhY2svX3ByZWx1ZGUuanMiLCIuLi8uLi8uLi8uLi8uLi8ucHduL2ZyaWRhL2xpYi9tb2R1bGUuanMiLCJmcmlkYS5qcyJdLCJuYW1lcyI6W10sIm1hcHBpbmdzIjoiQUFBQTtBQ0FBO0FBQ0E7QUFDQTtBQUNBO0FBQ0E7QUFDQTtBQUNBO0FBQ0E7QUFDQTtBQUNBO0FBQ0E7O0FDVkE7QUFDQTtBQUNBO0FBQ0E7QUFDQTtBQUNBO0FBQ0E7QUFDQTtBQUNBO0FBQ0E7QUFDQTtBQUNBO0FBQ0E7QUFDQTtBQUNBO0FBQ0E7QUFDQTtBQUNBO0FBQ0E7QUFDQTtBQUNBO0FBQ0E7QUFDQSIsImZpbGUiOiJnZW5lcmF0ZWQuanMiLCJzb3VyY2VSb290IjoiIn0=
