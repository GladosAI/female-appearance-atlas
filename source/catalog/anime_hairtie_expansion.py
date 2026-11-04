"""V30: varied tie routes informed by character hair motifs, on original adult models."""
from catalog_content import CATALOG
from accessory_hairstyle_expansion import hairstyle,HAIR_ACCESSORY_GROUPS
next(g for g in HAIR_ACCESSORY_GROUPS if g['id']=='tie')['count']=48
MOTIFS=[{'id':'kumihimo','name':'组绳与长带结','count':8,'reference':'三叶','url':'https://kiminona.com/'},{'id':'paired_bows','name':'双侧蝴蝶结与飘带','count':8,'reference':'鹿目圆','url':'https://www.madoka-magica.com/tv/archives/character/'},{'id':'sidelock_wrap','name':'侧鬓与局部交叉缠绳','count':8,'reference':'Lain','url':'https://www.nbcuni.co.jp/rondorobe/anime/lain/'},{'id':'forelock_tuft','name':'额前束发与冲天揪','count':8,'reference':'酒精喵喵（アルねこ）','url':'https://yanineko-anime.com/'}]
hairstyle('tie','''
组绳长尾双辫盘发|long-kumihimo braided updo|斜后面|红色扁编组绳|后脑双辫汇合处|两条成年低辫绕成后脑盘髻，红色扁编绳在汇合处形成一枚清楚蝶结，长短带尾完整留在肩上；局部放大绳结
双色编绳侧结低髻|two-tone-cord side-knot low bun|斜后面|双色扁编绳|后颈低髻侧面|单个紧凑低髻外有双色平编绳，侧边短结和两条窄垂尾；绳股编纹与入髻处清楚
细组绳半扎长带结|fine-kumihimo half-up long bow|斜后面|细扁编绳长尾结|后脑半扎根部|肩胛长直发上半后拢，细组绳包住小束根后结出小环和两条长尾，长尾不充当发束
宽织带交叠高束髻|wide-woven-tie high folded bun|斜后面|宽织带平结|头后高束髻根|中长发折成高位扁髻，宽织带在髻根交叠后形成扁平结，两个布尾完全展开可见
双绳并绕低马尾结|parallel-double-cord low ponytail|斜后面|两色独立细编绳|低马尾束根|肩胛长低尾由两根不同颜色细编绳并绕根部，侧面小结和四枚短绳尾分开可辨
长带交编单辫收尾|ribbon-interwoven braid-end tie|斜侧后面|细长缎带|单辫中段至辫尾|侧三股辫中交编一条细长缎带，辫尾打小蝶结，带尾与散开的短发尾分别可见
扁绳后脑双结盘髻|flat-cord double-knot updo|背面略侧|两段扁编绳结|左右小髻根|后脑左右各一个小扁髻，两处各系一枚小编绳结，短带尾对称，两个结位保持独立
绳结包根侧拢短尾|knotted-cord side-gathered short tail|斜侧后面|圆编绳结|耳后侧束根|锁骨发向一侧耳后收成短尾，粗细适中的圆编绳绕束根，侧外小结与两条短尾清楚
宽缎蝶结短高双尾|wide-satin-bow short twin tails|背面略侧|两枚宽缎蝶结发绳|左右耳上束根|肩上短高双马尾各用独立弹力圈固定，宽缎蝶结在圈外，结环立体但不遮住扎根
窄带长环低双尾|narrow-long-loop low twin tails|斜后面|两枚窄带长环结|左右后颈束根|齐肩低双尾外各一枚长环窄带结，细长结环与短带尾分开，左右弹力固定点独立
双层蝶结卷发双尾|double-layer-bow curly twin tails|斜后面|两枚双层布蝶结|左右中位束根|及肩卷发分成左右中位双尾，外侧各有大环小环叠层布结，底部弹力圈可见
不对称结饰侧马尾|asymmetric-bow side ponytail|斜侧后面|单枚不对称缎结|一侧高马尾根|一侧高尾配一大一小结环和两条不同长度缎尾，结体与发圈连接点放在可见外侧
飘带结半扎双束|streamer-bow half-up twin sections|背面略侧|两枚短环长尾发绳|后脑两处半扎根|上半发左右各扎一束，短蝶环下各有两条完整飘带，下半发保持披散并与带尾分开
小结发绳双丸子|small-bow-tie twin buns|背面略侧|两枚小缎带结发绳|左右低髻根|两枚低丸子髻根外分别系小缎结，结只装饰固定圈，发团完整位于圈上方
垂尾发结低侧髻|drop-tail-bow low side bun|斜侧后面|长垂尾布结|一侧后颈低髻根|单侧低髻外有一枚短结环和两条长垂尾，布结根固定髻根，垂尾在肩前或肩侧完整可见
左右异色短结双尾|two-tone-independent bow twin tails|背面略侧|两枚异色短结弹力圈|左右中位束根|两条短双尾分别配不同色但相同结构的小蝶结，两个弹力圈独立闭合，后颈无连接绳
单侧长鬓交叉绳结|cross-wrapped long sidelock|斜前侧面|一根窄深色软绳|一侧长鬓发中段|不对称短波波一侧保留长鬓发，软绳只围这一束鬓发形成两处小X，结位在束末，耳朵与绳尾完整
短鬓双段缠结造型|two-stage short-sidelock cord|斜前侧面|两枚细软绳结|耳前短鬓束中段|短层次发一侧耳前留一束细鬓，两个独立细结分段收束，段间短发自然鼓起
宽带斜绕单侧鬓束|wide-ribbon diagonal sidelock wrap|侧面略前|一条扁窄织带|一侧耳前长鬓|齐颈短发一侧长鬓外有扁带斜绕成两道间隔带段，末端小结不触及耳廓，发尾完整
双色细绳交编鬓辫|two-cord interwoven side braid|斜前侧面|两色细编绳|耳前小三股辫|一侧耳前编成细三股鬓辫，两根细绳随辫交编，辫尾用短结收尾，保留脸侧清晰轮廓
颊侧小束环结短发|cheek-side loop-tied short hair|侧面略前|细圆弹力绳|颊侧小发束|偏分齐耳短发，颊侧一小束头发在耳下用细圆绳固定成短松结，脸部不被绳遮挡
侧鬓螺旋绕线直发|spiral-cord straight sidelock|斜前侧面|细金色编绳|单侧直鬓发|齐肩直发一侧长鬓以细金绳螺旋绕束，绳段保持间距，小结与完整短绳尾在束末可见
双侧细鬓独立小结|separate tiny ties on twin sidelocks|斜前面|两根独立细发绳|左右耳前细鬓|中分齐肩发两侧耳前各留细鬓，分别用小绳结收束，左右不相连且不跨过面部
低位鬓束蝶结半披发|low-sidelock bow half-down hair|斜前侧面|细缎带小蝶结|一侧耳下鬓束|肩胛长披发的一侧鬓束单独低扎，小蝶结在耳下外侧，主体长发自然披散，完整鬓尾可见
额前短冲天揪长披发|short-upright forelock on loose hair|斜前面|细黑弹力发绳|前额发际后方小束根|成年额前一小撮头发向上扎成短尖束，细黑发绳围住真实小束根，剩余肩胛发披散，放大扎根
偏侧额前小揪短发|off-center forelock tuft on bob|斜前面|小号细弹力圈|一侧前顶发根|下巴波波在前额一侧扎短小向上发束，束根在发际后方，细圈与露出的额头分开可见
双额角细束上扎发|paired front-corner upward tufts|斜前面|两枚独立细发绳|左右额角根部|齐肩发左右额角各留小束向上扎起，短束在各自绳圈上方展开，两处固定点互不连接
前顶折环小揪半披发|small folded front-top hair loop|斜前侧面|细弹力发圈|前顶小发束根|前顶一小束头发向后折成小环，由细圈固定根部，少量短尾露出，主体发披散
额前细辫高扎短束|front-mini-braid upright tuft|斜前面|细圆发绳|前额小辫末端|前额一小束编成短细辫后向上收束，辫末小绳圈固定并留下短尖发尾，前额结构清楚
三股小束前顶聚扎|three-front-sections gathered tuft|斜前面|一枚小弹力圈|前顶三束交汇处|前额三条窄发片向前顶汇拢，以小圈共同固定成一撮短立束，三处发流方向与根部可见
宽软绳结额前束发|soft-cord-knot forelock tuft|斜前侧面|软圆编绳短结|前额发际后方束根|额前较宽小发片向上收成短束，软圆绳打小结，绳尾短且完整，不垂到眉眼
发际后小束配低尾|front-tuft with low ponytail|斜前侧面|两枚独立细弹力圈|前顶小束与后颈尾根|前额小束向上扎成短揪，其他中发独立低扎成短马尾，前后两枚发圈各固定自己的发束
''')
for i,e in enumerate(CATALOG[-32:]):
    motif=MOTIFS[i//8]
    aliases={'kumihimo':['三叶','宫水三叶','Mitsuha'],'paired_bows':['小圆','鹿目圆','Madoka'],'sidelock_wrap':['Lain','玲音','岩仓玲音'],'forelock_tuft':['酒精喵喵','酒精猫猫','アルねこ']}[motif['id']]
    e.update(aliases=aliases,added_in='30.0',anime_hairtie_reference=True,hair_tie_motif=motif['id'],hair_tie_motif_name=motif['name'],motif_source_name=motif['reference'],motif_source_url=motif['url'],hair_tie_detail_inset=True,
      note='观察组绳、带结、侧鬓缠绕和额前局部扎束如何改变轮廓。图例将参考中的发绳结构用于25岁以上原创成年角色，保留完整头顶、绳结、扎根与发尾；放大图只显示同一固定点。先确认发束在圈内收拢，再画绳圈、结环及带尾。')
