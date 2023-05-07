(function(){"use strict";var e={6948:function(e,t,r){var o=r(8315),i=r(7195),s=function(){var e=this,t=e._self._c;return t("div",{attrs:{id:"app"}},[t("router-view")],1)},a=[],n=r(1001),d={},l=(0,n.Z)(d,s,a,!1,null,null,null),c=l.exports,u=r(2241),m=function(){var e=this,t=e._self._c;return t("div",{staticClass:"container"},[t("div",{staticClass:"row"},[t("div",{staticClass:"col-sm-10"},[t("h1",[e._v("CVE Table")]),t("hr"),t("br"),t("br"),e.showMessage?t("alert",{attrs:{message:e.message}}):e._e(),t("button",{directives:[{name:"b-modal",rawName:"v-b-modal.cve-modal",modifiers:{"cve-modal":!0}}],staticClass:"btn btn-success btn-sm",attrs:{type:"button"}},[e._v("Add CVE")]),t("br"),t("br"),t("table",{staticClass:"table table-hover"},[e._m(0),t("tbody",e._l(e.VulnerabilityCVE,(function(r,o){return t("tr",{key:o},[t("td",[e._v(e._s(r.cve))]),t("td",[e._v(e._s(r.types))]),t("td",[e._v(e._s(r.severity))]),t("td",[e._v(e._s(r.score))]),t("td",[r.remediation?t("span",[e._v("Available")]):t("span",[e._v("None")])]),t("td",[t("div",{staticClass:"btn-group",attrs:{role:"group"}},[t("button",{directives:[{name:"b-modal",rawName:"v-b-modal.cve-update-modal",modifiers:{"cve-update-modal":!0}}],staticClass:"btn btn-warning btn-sm",attrs:{type:"button"},on:{click:function(t){return e.editCVE(r)}}},[e._v(" Update ")]),t("button",{staticClass:"btn btn-danger btn-sm",attrs:{type:"button"},on:{click:function(t){return e.onDeleteCVE(r)}}},[e._v(" Delete ")])])])])})),0)])],1)]),t("b-modal",{ref:"addCVEModal",attrs:{id:"cve-modal",title:"Add a new cve","hide-footer":""}},[t("b-form",{staticClass:"w-100",on:{submit:e.onSubmit,reset:e.onReset}},[t("b-form-group",{attrs:{id:"form-cve-group",label:"CVE:","label-for":"form-cve-input"}},[t("b-form-input",{attrs:{id:"form-cve-input",type:"text",required:"",placeholder:"Enter cve"},model:{value:e.addCVEForm.cve,callback:function(t){e.$set(e.addCVEForm,"cve",t)},expression:"addCVEForm.cve"}})],1),t("b-form-group",{attrs:{id:"form-types-group",label:"Types:","label-for":"form-types-input"}},[t("b-form-input",{attrs:{id:"form-types-input",type:"text",required:"",placeholder:"Enter types"},model:{value:e.addCVEForm.types,callback:function(t){e.$set(e.addCVEForm,"types",t)},expression:"addCVEForm.types"}})],1),t("b-form-group",{attrs:{id:"form-severity-group",label:"Severity:","label-for":"form-severity-input"}},[t("b-form-input",{attrs:{id:"form-severity-input",type:"text",required:"",placeholder:"Enter severity"},model:{value:e.addCVEForm.severity,callback:function(t){e.$set(e.addCVEForm,"severity",t)},expression:"addCVEForm.severity"}})],1),t("b-form-group",{attrs:{id:"form-score-group",label:"Score:","label-for":"form-score-input"}},[t("b-form-input",{attrs:{id:"form-score-input",type:"text",required:"",placeholder:"Enter score"},model:{value:e.addCVEForm.score,callback:function(t){e.$set(e.addCVEForm,"score",t)},expression:"addCVEForm.score"}})],1),t("b-form-group",{attrs:{id:"form-remediation-group"}},[t("b-form-checkbox-group",{attrs:{id:"form-checks"},model:{value:e.addCVEForm.remediation,callback:function(t){e.$set(e.addCVEForm,"remediation",t)},expression:"addCVEForm.remediation"}},[t("b-form-checkbox",{attrs:{value:"true"}},[e._v("Read?")])],1)],1),t("b-button-group",[t("b-button",{attrs:{type:"submit",variant:"primary"}},[e._v("Submit")]),t("b-button",{attrs:{type:"reset",variant:"danger"}},[e._v("Cancel")])],1)],1)],1),t("b-modal",{ref:"editCVEModal",attrs:{id:"cve-update-modal",title:"Update","hide-footer":""}},[t("b-form",{staticClass:"w-100",on:{submit:e.onSubmitUpdate,reset:e.onResetUpdate}},[t("b-form-group",{attrs:{id:"form-cve-edit-group",label:"CVE:","label-for":"form-cve-edit-input"}},[t("b-form-input",{attrs:{id:"form-cve-edit-input",type:"text",required:"",placeholder:"Enter cve"},model:{value:e.editForm.cve,callback:function(t){e.$set(e.editForm,"cve",t)},expression:"editForm.cve"}})],1),t("b-form-group",{attrs:{id:"form-types-edit-group",label:"Type:","label-for":"form-types-edit-input"}},[t("b-form-input",{attrs:{id:"form-types-edit-input",type:"text",required:"",placeholder:"Enter types"},model:{value:e.editForm.types,callback:function(t){e.$set(e.editForm,"types",t)},expression:"editForm.types"}})],1),t("b-form-group",{attrs:{id:"form-severity-edit-group",label:"Severity:","label-for":"form-severity-edit-input"}},[t("b-form-input",{attrs:{id:"form-serverity-edit-input",type:"text",required:"",placeholder:"Enter severity"},model:{value:e.editForm.severity,callback:function(t){e.$set(e.editForm,"severity",t)},expression:"editForm.severity"}})],1),t("b-form-group",{attrs:{id:"form-score-edit-group",label:"Score:","label-for":"form-score-edit-input"}},[t("b-form-input",{attrs:{id:"form-score-edit-input",type:"text",required:"",placeholder:"Enter score"},model:{value:e.editForm.score,callback:function(t){e.$set(e.editForm,"score",t)},expression:"editForm.score"}})],1),t("b-form-group",{attrs:{id:"form-remediation-edit-group"}},[t("b-form-checkbox-group",{attrs:{id:"form-checks"},model:{value:e.editForm.remediation,callback:function(t){e.$set(e.editForm,"remediation",t)},expression:"editForm.remediation"}},[t("b-form-checkbox",{attrs:{value:"true"}},[e._v("Remedation available?")])],1)],1),t("b-button-group",[t("b-button",{attrs:{type:"submit",variant:"primary"}},[e._v("Update")]),t("b-button",{attrs:{type:"reset",variant:"danger"}},[e._v("Cancel")])],1)],1)],1)],1)},p=[function(){var e=this,t=e._self._c;return t("thead",[t("tr",[t("th",{attrs:{scope:"col"}},[e._v("CVE")]),t("th",{attrs:{scope:"col"}},[e._v("Types")]),t("th",{attrs:{scope:"col"}},[e._v("Severity")]),t("th",{attrs:{scope:"col"}},[e._v("Score")]),t("th",{attrs:{scope:"col"}},[e._v("Remediation")]),t("th")])])}],v=r(306),f=function(){var e=this,t=e._self._c;return t("div",[t("b-alert",{attrs:{variant:"success",show:""}},[e._v(e._s(e.message))]),t("br")],1)},b=[],h={props:["message"]},y=h,g=(0,n.Z)(y,f,b,!1,null,null,null),C=g.exports,V={data(){return{VulnerabilityCVE:[],addCVEForm:{cve:"",types:"",severity:"",score:"",remediation:[]},editForm:{id:"",cve:"",types:"",severity:"",score:"",remediation:[]},message:"",showMessage:!1}},components:{alert:C},methods:{getVulnerabilityCVE(){const e="http://127.0.0.1:5000/api/cve";v.Z.get(e).then((e=>{this.VulnerabilityCVE=e.data.VulnerabilityCVE})).catch((e=>{console.error(e)}))},addCVE(e){const t="http://127.0.0.1:5000/api/cve";v.Z.post(t,e).then((()=>{this.getVulnerabilityCVE(),this.message="CVE added!",this.showMessage=!0})).catch((e=>{console.log(e),this.getVulnerabilityCVE()}))},initForm(){this.addCVEForm.cve="",this.addCVEForm.types="",this.addCVEForm.severity="",this.addCVEForm.score="",this.addCVEForm.remediation=!1,this.editForm.id="",this.editForm.cve="",this.editForm.types="",this.editForm.severity="",this.editForm.score="",this.editForm.remediation=!1},onSubmit(e){e.preventDefault(),this.$refs.addCVEModal.hide();let t=!1;this.addCVEForm.remediation&&(t=!0);const r={cve:this.addCVEForm.cve,types:this.addCVEForm.types,severity:this.addCVEForm.severity,score:this.addCVEForm.score,remediation:t};this.addCVE(r),this.initForm()},editCVE(e){this.editForm=e},onSubmitUpdate(e){e.preventDefault(),this.$refs.editCVEModal.hide();let t=!1;this.editForm.remediation&&(t=!0);const r={cve:this.editForm.cve,types:this.editForm.types,severity:this.editForm.severity,score:this.editForm.score,remediation:t};this.updateCVE(r,this.editForm.id)},updateCVE(e,t){const r=`http://localhost:5000/api/cve/${t}`;v.Z.put(r,e).then((()=>{this.getVulnerabilityCVE(),this.message="CVE updated!",this.showMessage=!0})).catch((e=>{console.error(e),this.getVulnerabilityCVE()}))},onResetUpdate(e){e.preventDefault(),this.$refs.editCVEModal.hide(),this.initForm(),this.getVulnerabilityCVE()},removeCVE(e){const t=`http://localhost:5000/api/cve/${e}`;v.Z["delete"](t).then((()=>{this.getVulnerabilityCVE(),this.message="CVE removed!",this.showMessage=!0})).catch((e=>{console.error(e),this.getVulnerabilityCVE()}))},onDeleteCVE(e){this.removeCVE(e.id)},onReset(e){e.preventDefault(),this.$refs.addCVEModal.hide(),this.initForm()}},created(){this.getVulnerabilityCVE()}},E=V,F=(0,n.Z)(E,m,p,!1,null,null,null),_=F.exports,x=function(){var e=this,t=e._self._c;return t("div",{staticClass:"container"},[t("button",{staticClass:"btn btn-primary",attrs:{type:"button"}},[e._v(e._s(e.msg))])])},k=[],w={name:"Ping-pong",data(){return{msg:""}},methods:{getMessage(){const e="http://0.0.0.0:5000/api/ping";v.Z.get(e).then((e=>{this.msg=e.data})).catch((e=>{console.error(e)}))}},created(){this.getMessage()}},$=w,M=(0,n.Z)($,x,k,!1,null,null,null),S=M.exports;i["default"].use(u.ZP);var O=new u.ZP({mode:"history",base:"/",routes:[{path:"/cve",name:"cve",component:_},{path:"/ping",name:"Ping",component:S}]});i["default"].use(o.ZPm),i["default"].config.productionTip=!1,new i["default"]({router:O,render:e=>e(c)}).$mount("#app")}},t={};function r(o){var i=t[o];if(void 0!==i)return i.exports;var s=t[o]={exports:{}};return e[o](s,s.exports,r),s.exports}r.m=e,function(){var e=[];r.O=function(t,o,i,s){if(!o){var a=1/0;for(c=0;c<e.length;c++){o=e[c][0],i=e[c][1],s=e[c][2];for(var n=!0,d=0;d<o.length;d++)(!1&s||a>=s)&&Object.keys(r.O).every((function(e){return r.O[e](o[d])}))?o.splice(d--,1):(n=!1,s<a&&(a=s));if(n){e.splice(c--,1);var l=i();void 0!==l&&(t=l)}}return t}s=s||0;for(var c=e.length;c>0&&e[c-1][2]>s;c--)e[c]=e[c-1];e[c]=[o,i,s]}}(),function(){r.n=function(e){var t=e&&e.__esModule?function(){return e["default"]}:function(){return e};return r.d(t,{a:t}),t}}(),function(){r.d=function(e,t){for(var o in t)r.o(t,o)&&!r.o(e,o)&&Object.defineProperty(e,o,{enumerable:!0,get:t[o]})}}(),function(){r.g=function(){if("object"===typeof globalThis)return globalThis;try{return this||new Function("return this")()}catch(e){if("object"===typeof window)return window}}()}(),function(){r.o=function(e,t){return Object.prototype.hasOwnProperty.call(e,t)}}(),function(){r.r=function(e){"undefined"!==typeof Symbol&&Symbol.toStringTag&&Object.defineProperty(e,Symbol.toStringTag,{value:"Module"}),Object.defineProperty(e,"__esModule",{value:!0})}}(),function(){var e={143:0};r.O.j=function(t){return 0===e[t]};var t=function(t,o){var i,s,a=o[0],n=o[1],d=o[2],l=0;if(a.some((function(t){return 0!==e[t]}))){for(i in n)r.o(n,i)&&(r.m[i]=n[i]);if(d)var c=d(r)}for(t&&t(o);l<a.length;l++)s=a[l],r.o(e,s)&&e[s]&&e[s][0](),e[s]=0;return r.O(c)},o=self["webpackChunkclient"]=self["webpackChunkclient"]||[];o.forEach(t.bind(null,0)),o.push=t.bind(null,o.push.bind(o))}();var o=r.O(void 0,[998],(function(){return r(6948)}));o=r.O(o)})();
//# sourceMappingURL=app.efeb71bb.js.map