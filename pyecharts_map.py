# coding=utf-8

# pip install git+https://github.com/pyecharts/pyecharts.git
# pyecharts (1.0.0)


from pyecharts import options as opts
from pyecharts.charts import Map

names = ['西藏', '青海', '宁夏', '海南', '甘肃', '贵州', '新疆', '云南', '重庆', '吉林', '山西', '天津', '江西', '广西', '陕西', '黑龙江', '内蒙古', '安徽',
         '北京', '福建', '上海', '湖北', '湖南', '四川', '辽宁', '河北', '河南', '浙江', '山东', '江苏', '广东']
values = [605.83, 1670.44, 2102.21, 2522.66, 5020.37, 5701.84, 6610.05, 8893.12, 10011.37, 10568.83, 11237.55, 11307.28,
          11702.82, 11720.87, 12512.3, 12582, 14359.88, 15300.65, 16251.93, 17560.18, 19195.69, 19632.26, 19669.56,
          21026.68, 22226.7, 24515.76, 26931.03, 32318.85, 45361.85, 49110.27, 53210.28]
range_color = ["#D6EAF8", "#00FFFF"]

cmap = (Map() 
    .add("商家A", [list(z) for z in zip(names, values)], "china", is_map_symbol_show=False) 
    .set_global_opts(
    title_opts=opts.TitleOpts(title="Map-VisualMap（连续型）"),
    legend_opts=opts.LegendOpts(is_show=False),
    visualmap_opts=opts.VisualMapOpts(min_=0, max_=60000, range_color=range_color)))

cmap.render('cmap.html')
