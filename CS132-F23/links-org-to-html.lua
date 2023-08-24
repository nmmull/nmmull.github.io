function Link(el)
  if not (el.target:sub(1, 7) == "http://" or el.target:sub(1, 8) == "https://") then
     el.target = string.gsub(el.target, "%.org", ".html")
  end
  return el
end
