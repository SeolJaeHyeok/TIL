!function(e){var r={};function t(n){if(r[n])return r[n].exports;var c=r[n]={i:n,l:!1,exports:{}};return e[n].call(c.exports,c,c.exports,t),c.l=!0,c.exports}t.m=e,t.c=r,t.d=function(e,r,n){t.o(e,r)||Object.defineProperty(e,r,{enumerable:!0,get:n})},t.r=function(e){"undefined"!=typeof Symbol&&Symbol.toStringTag&&Object.defineProperty(e,Symbol.toStringTag,{value:"Module"}),Object.defineProperty(e,"__esModule",{value:!0})},t.t=function(e,r){if(1&r&&(e=t(e)),8&r)return e;if(4&r&&"object"==typeof e&&e&&e.__esModule)return e;var n=Object.create(null);if(t.r(n),Object.defineProperty(n,"default",{enumerable:!0,value:e}),2&r&&"string"!=typeof e)for(var c in e)t.d(n,c,function(r){return e[r]}.bind(null,c));return n},t.n=function(e){var r=e&&e.__esModule?function(){return e.default}:function(){return e};return t.d(r,"a",r),r},t.o=function(e,r){return Object.prototype.hasOwnProperty.call(e,r)},t.p="/",t(t.s=15)}([function(e,r){e.exports=require("react/jsx-runtime")},function(e,r){e.exports=require("react")},function(e,r){e.exports=require("react-router-dom")},function(e,r,t){e.exports=t(14)},function(e,r){e.exports=require("react-redux")},function(e,r){e.exports=require("redux-saga/effects")},function(e,r){e.exports=require("redux")},function(e,r){e.exports=require("react-dom/server")},function(e,r){e.exports=require("express")},function(e,r){e.exports=require("axios")},function(e,r){e.exports=require("path")},function(e,r){e.exports=require("redux-saga")},function(e,r){e.exports=require("fs")},function(e,r){e.exports=require("redux-thunk")},function(e,r){e.exports=require("regenerator-runtime")},function(e,r,t){"use strict";t.r(r);var n=t(3),c=t.n(n);function s(e,r,t,n,c,s,u){try{var o=e[s](u),i=o.value}catch(e){return void t(e)}o.done?r(i):Promise.resolve(i).then(n,c)}function u(e){return function(){var r=this,t=arguments;return new Promise((function(n,c){var u=e.apply(r,t);function o(e){s(u,n,c,o,i,"next",e)}function i(e){s(u,n,c,o,i,"throw",e)}o(void 0)}))}}var o=t(1),i=t.n(o),a=t(7),l=t.n(a),p=t(8),d=t.n(p),f=t(2),j=t(0),b=function(){return Object(j.jsx)("div",{className:"Red",children:"Red"})},x=function(){return Object(j.jsx)(b,{})},O=function(){return Object(j.jsx)("div",{className:"Blue",children:"Blue"})},h=function(){return Object(j.jsx)(O,{})},v=function(){return Object(j.jsxs)("ul",{children:[Object(j.jsx)("li",{children:Object(j.jsx)(f.Link,{to:"/red",children:"Red"})}),Object(j.jsx)("li",{children:Object(j.jsx)(f.Link,{to:"/blue",children:"Blue"})}),Object(j.jsx)("li",{children:Object(j.jsx)(f.Link,{to:"/users",children:"Users"})})]})},m=t(4),y=function(e){var r=e.user,t=r.email,n=r.name,c=r.username;return Object(j.jsxs)("div",{children:[Object(j.jsxs)("h1",{children:[c," (",n,")"]}),Object(j.jsxs)("p",{children:[Object(j.jsx)("b",{children:"e-mail:"})," ",t]})]})},S=Object(o.createContext)(null),g=S,E=function(e){var r=e.resolve,t=Object(o.useContext)(S);return t?(t.done||t.promises.push(Promise.resolve(r())),null):null};function _(e,r,t){return r in e?Object.defineProperty(e,r,{value:t,enumerable:!0,configurable:!0,writable:!0}):e[r]=t,e}function R(e,r){var t=Object.keys(e);if(Object.getOwnPropertySymbols){var n=Object.getOwnPropertySymbols(e);r&&(n=n.filter((function(r){return Object.getOwnPropertyDescriptor(e,r).enumerable}))),t.push.apply(t,n)}return t}function w(e){for(var r=1;r<arguments.length;r++){var t=null!=arguments[r]?arguments[r]:{};r%2?R(Object(t),!0).forEach((function(r){_(e,r,t[r])})):Object.getOwnPropertyDescriptors?Object.defineProperties(e,Object.getOwnPropertyDescriptors(t)):R(Object(t)).forEach((function(r){Object.defineProperty(e,r,Object.getOwnPropertyDescriptor(t,r))}))}return e}var P=t(9),U=t.n(P),k=t(5),T=c.a.mark(N),q=c.a.mark(A),G="user/GET_USER",C=function(e){return{type:"users/GET_USERS_FAILURE",error:!0,payload:e}},D=function(e){return{type:G,payload:e}},L=function(e){return U.a.get("https://jsonplaceholder.typicode.com/users/".concat(e))};function N(e){var r;return c.a.wrap((function(t){for(;;)switch(t.prev=t.next){case 0:return t.prev=0,t.next=3,Object(k.call)(L,e.payload);case 3:return r=t.sent,t.next=6,Object(k.put)({type:"user/GET_USER_SUCCESS",payload:r.data});case 6:t.next=12;break;case 8:return t.prev=8,t.t0=t.catch(0),t.next=12,Object(k.put)({type:"user/GET_USER_FAILURE",payload:t.t0,error:!0});case 12:case"end":return t.stop()}}),T,null,[[0,8]])}function A(){return c.a.wrap((function(e){for(;;)switch(e.prev=e.next){case 0:return e.next=2,Object(k.takeEvery)(G,N);case 2:case"end":return e.stop()}}),q)}var F={users:null,loading:{users:!1,user:!1},error:{users:null,user:null}};var I=function(){var e=arguments.length>0&&void 0!==arguments[0]?arguments[0]:F,r=arguments.length>1?arguments[1]:void 0;switch(r.type){case"users/GET_USERS_PENDING":return w(w({},e),{},{loading:w(w({},e.loading),{},{users:!0}),error:w(w({},e.error),{},{users:null})});case"users/GET_USERS_SUCCESS":return w(w({},e),{},{loading:w(w({},e.loading),{},{users:!1}),users:r.payload.data});case"users/GET_USERS_FAILURE":return w(w({},e),{},{loading:w(w({},e.loading),{},{users:!1}),error:w(w({},e.error),{},{users:r.payload})});case G:return w(w({},e),{},{loading:w(w({},e.loading),{},{user:!0}),error:w(w({},e.error),{},{user:null})});case"user/GET_USER_SUCCESS":return w(w({},e),{},{loading:w(w({},e.loading),{},{user:!1}),user:r.payload});case"user/GET_USER_FAILURE":return w(w({},e),{},{loading:w(w({},e.loading),{},{user:!1}),error:w(w({},e.error),{},{user:r.payload})});default:return e}},M=function(e){var r,t,n=e.id,c=Object(m.useSelector)((function(e){return e.users.user})),s=Object(m.useDispatch)();return r=function(){return s(D(n))},(t=Object(o.useContext)(S))&&!t.done&&t.promises.push(Promise.resolve(r())),Object(o.useEffect)((function(){c&&c.id===parseInt(n,10)||s(D(n))}),[s,n,c]),c?Object(j.jsx)(y,{user:c}):null},B=function(e){var r=e.users;return r?Object(j.jsx)("div",{children:Object(j.jsx)("ul",{children:r.map((function(e){return Object(j.jsx)("li",{children:Object(j.jsx)(f.Link,{to:"/users/".concat(e.id),children:e.username})},e.id)}))})}):null},J=i.a.useEffect,Y=Object(m.connect)((function(e){return{users:e.users.users}}),{getUsers:function(){return function(){var e=u(c.a.mark((function e(r){var t;return c.a.wrap((function(e){for(;;)switch(e.prev=e.next){case 0:return e.prev=0,r({type:"users/GET_USERS_PENDING"}),e.next=4,U.a.get("https://jsonplaceholder.typicode.com/users");case 4:t=e.sent,r({type:"users/GET_USERS_SUCCESS",payload:t}),e.next=12;break;case 8:throw e.prev=8,e.t0=e.catch(0),r(C(e.t0)),e.t0;case 12:case"end":return e.stop()}}),e,null,[[0,8]])})));return function(r){return e.apply(this,arguments)}}()}})((function(e){var r=e.users,t=e.getUsers;return J((function(){r||t()}),[t,r]),Object(j.jsxs)(j.Fragment,{children:[Object(j.jsx)(B,{users:r}),Object(j.jsx)(E,{resolve:t})]})})),$=function(){return Object(j.jsxs)(j.Fragment,{children:[Object(j.jsx)(Y,{}),Object(j.jsx)(f.Route,{path:"/users/:id",render:function(e){var r=e.match;return Object(j.jsx)(M,{id:r.params.id})}})]})};var z=function(){return Object(j.jsxs)("div",{children:[Object(j.jsx)(v,{}),Object(j.jsx)("hr",{}),Object(j.jsx)(f.Route,{path:"/red",component:x}),Object(j.jsx)(f.Route,{path:"/blue",component:h}),Object(j.jsx)(f.Route,{path:"/users",component:$})]})},H=t(10),K=t.n(H),Q=t(12),V=t.n(Q),W=t(6),X=t(11),Z=t.n(X),ee=t(13),re=t.n(ee),te=c.a.mark(ne);function ne(){return c.a.wrap((function(e){for(;;)switch(e.prev=e.next){case 0:return e.next=2,Object(k.all)([A()]);case 2:case"end":return e.stop()}}),te)}var ce=Object(W.combineReducers)({users:I}),se=JSON.parse(V.a.readFileSync(K.a.resolve("./build/asset-manifest.json"),"utf8")),ue=Object.keys(se.files).filter((function(e){return/chunk\.js$/.exec(e)})).map((function(e){return'<script src="'.concat(se.files[e],'"><\/script>')})).join("");function oe(e,r){return'<!DOCTYPE html>\n    <html lang="en">\n    <head>\n      <meta charset="utf-8" />\n      <link rel="shortcut icon" href="/favicon.ico" />\n      <meta\n        name="viewport"\n        content="width=device-width,initial-scale=1,shrink-to-fit=no"\n      />\n      <meta name="theme-color" content="#000000" />\n      <title>React App</title>\n      <link href="'.concat(se.files["main.css"],'" rel="stylesheet" />\n    </head>\n    <body>\n      <noscript>You need to enable JavaScript to run this app.</noscript>\n      <div id="root">\n        ').concat(e,"\n      </div>\n      ").concat(r,'\n      <script src="').concat(se.files["runtime-main.js"],'"><\/script>\n      ').concat(ue,'\n      <script src="').concat(se.files["main.js"],'"><\/script>\n    </body>\n    </html>\n      ')}var ie=d()(),ae=function(){var e=u(c.a.mark((function e(r,t,n){var s,u,o,i,a,p,d,b,x;return c.a.wrap((function(e){for(;;)switch(e.prev=e.next){case 0:return s={},u=Z()(),o=Object(W.createStore)(ce,Object(W.applyMiddleware)(re.a,u)),i=u.run(ne).toPromise(),a={done:!1,promises:[]},p=Object(j.jsx)(g.Provider,{value:a,children:Object(j.jsx)(m.Provider,{store:o,children:Object(j.jsx)(f.StaticRouter,{location:r.url,context:s,children:Object(j.jsx)(z,{})})})}),l.a.renderToStaticMarkup(p),o.dispatch(X.END),e.prev=8,e.next=11,i;case 11:return e.next=13,Promise.all(a.promises);case 13:e.next=18;break;case 15:return e.prev=15,e.t0=e.catch(8),e.abrupt("return",t.staus(500));case 18:a.done=!0,d=l.a.renderToString(p),b=JSON.stringify(o.getState()).replace(/</g,"\\u003c"),x="<script>__PRELOADED_STATE__ = ".concat(b,"<\/script>"),t.send(oe(d,x));case 23:case"end":return e.stop()}}),e,null,[[8,15]])})));return function(r,t,n){return e.apply(this,arguments)}}(),le=d.a.static(K.a.resolve("./build"),{index:!1});ie.use(le),ie.use(ae),ie.listen(5e3,(function(){console.log("Running on http://localhost:5000")}))}]);