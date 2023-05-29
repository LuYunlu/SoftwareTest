import { stringify } from "json5";
 
// 按照二进制读取文件
export function readFile(file) {
  return new Promise((resolve) => {
    let reader = new FileReader();
    reader.readAsBinaryString(file);
    reader.onload = (e) => {
      resolve(e.target.result);
    };
  });
}
 
// 字段对应表
export let character = {
  date: {
    text: "date",
    type: "string",
  },
  active_shards: {
    text: "health_active_shards",
    type: "number",
  }
};
 
// 时间字符串格式化
export function formatTime(str, tpl) {
  let arr = str.match(/\d+/g).map((item) => {
    return item.length < 2 ? "0" + item : item;
  });
  tpl = tpl || "{0}年{1}月{2}日 {3}时{4}分{5}秒";
  return tpl.replace(/\{(\d+)\}/g, (_, group) => {
    return arr[group] || "00";
  });
}
