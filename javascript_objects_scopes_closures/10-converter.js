#!/usr/bin/node
exports.converter = function (base) {
   if (base < 2 || base > 36) {
    return 'Invalid base' ;
   }
   result = '';
   remainder = 0;

   while (num > 0) {
    remainder = num % base;
    result = remainder.toString(base) + result;
    num = Math.floor(num / base);
   }
   return result || '0';
}
