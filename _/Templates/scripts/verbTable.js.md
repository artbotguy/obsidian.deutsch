function verbTable(tags) {
  const pages = dv.pages('#verbvalenz');
  const cols = {};
  tags.forEach(t => cols[t] = []);
  
  pages.forEach(p => {
    tags.forEach(t => {
      if (p.file.etags.includes(`#vv_vk_${t}`)) {
        cols[t].push(p.file.link);
      }
    });
  });
  
  const max = Math.max(...Object.values(cols).map(c => c.length));
  const data = Array.from({length: max}, (_, i) => 
    Object.values(cols).map(c => c[i] || "")
  );
  
  dv.table(tags, data);
}

// Передаем параметры из input
if (input && input.tags) {
  verbTable(input.tags);
}