// 设置异步延迟间隔
export function delay(interval = 0) {
    return new Promise((resolve) => {
      let timer = setTimeout((_) => {
        clearTimeout(timer);                                                                                                          
        resolve();
      }, interval);
    });
  }