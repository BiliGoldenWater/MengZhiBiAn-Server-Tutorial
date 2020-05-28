---
typora-root-url: ..\..\pics
---

# 论集成动力(上)

快速跳转: 论集成动力下

------

> 当集成动力、集成管道同时存在时，其他物流管道就几乎没有存在的意义了。
>
> 如果有更好的储物模组，且装有集成合成学和集成终端，那么；连AE2都毫无竞争力。

集成动力系列可以说是自动化和物流网络中性能最强，造价最低的。它拥有几乎无上限的能量、物品、流体和红石管道，支持远程、跨世界传输，以及极其强大的筛选和自动化功能。除了无法兼容IC2系列的EU电缆，和MEK的导热线缆，以及拥有最大2,147,483,647的能量上限外，它无所不能。（甚至支持神秘时代！可惜不支持染料魔法）

游戏内自带《论继承动力》一书，作为mod的说明书。另外还有mod的wiki，可以自行查阅。

本章节主要简单介绍集成动力的开局和简单的管道配置。关于自动化的章节，将于集成动力下进行更详细的讲解。

## 第一节 入门

要开始踏入集成动力的大门，首先你需要找到一颗重要的植物——门瑞欧树。

![门瑞欧树 (Menril tree)](https://i.mcmod.cn/class/cover/20171128/1511814021_19138_JEnH.jpg)

门瑞欧的原木分为[![富集门瑞欧原木 (Enriched Menril Wood)](https://i.mcmod.cn/item/icon/32x32/6/63165.png)](https://www.mcmod.cn/item/63165.html)[富集门瑞欧原木](https://www.mcmod.cn/item/63165.html)和普通[![门瑞欧原木 (Menril Wood)](https://i.mcmod.cn/item/icon/32x32/6/63164.png)](https://www.mcmod.cn/item/63164.html)[门瑞欧原木](https://www.mcmod.cn/item/63164.html)两种，一棵树内通常含有一块富集原木。破坏富集原木后可以获得[![门瑞欧结晶碎块 (Crystalized Menril Chunk)](https://i.mcmod.cn/item/icon/32x32/6/63184.png)](https://www.mcmod.cn/item/63184.html)[门瑞欧结晶碎块](https://www.mcmod.cn/item/63184.html)，这是所有集成动力的物品都需要的原料。

如果你没有看到富集原木也没有关系，普通的门瑞欧原木也可以通过一些方式产出[![门瑞欧结晶方块 (Block of Crystalized Menril)](https://i.mcmod.cn/item/icon/32x32/6/63169.png)](https://www.mcmod.cn/item/63169.html)[门瑞欧结晶方块](https://www.mcmod.cn/item/63169.html)，只要能找到门欧瑞树木即可开始游玩集成动力模组。

随后，你最好能制作一台[![烘干池 (Drying Basin)](https://i.mcmod.cn/item/icon/32x32/6/63172.png)](https://www.mcmod.cn/item/63172.html)[烘干池](https://www.mcmod.cn/item/63172.html)和一台[![挤压机 (Squeezer)](https://i.mcmod.cn/item/icon/32x32/6/63173.png)](https://www.mcmod.cn/item/63173.html)[挤压机](https://www.mcmod.cn/item/63173.html)。具体的合成方式可以在NEI中自行查阅，或点击连接转到mcmod中查看。

你需要将烘干池和挤压机放在一起，或者使用液体管道相连。随后在挤压机中放入门瑞欧原木，并在挤压机正中心上方跳跃！在大约4~5次跳跃后，就可以完成挤压，门瑞欧树脂会自动流入烘干池，并烘干成门瑞欧结晶方块。

你可以通过对挤压机输出红石信号来重置挤压机，比如在上面放一个按钮，或者粗暴的将其拆掉重放。你也可以制作电动版的来解放双手，提高效率。

## 第二节 初窥门径

#### 模组物品

在这个模组中，万物离不开[![逻辑线缆 (Logic Cable)](https://i.mcmod.cn/item/icon/32x32/6/63155.png)](https://www.mcmod.cn/item/63155.html)[逻辑线缆](https://www.mcmod.cn/item/63155.html)。逻辑线缆可以传递频道和网络，从而传递所有的一切——物品、能量、流体和红石信号！

但是光有线缆也是不行的。如果你要传输物品，至少需要有一个![物品接口 (Item Interface)](https://i.mcmod.cn/item/icon/32x32/17/177480.png)[物品接口](https://www.mcmod.cn/item/177480.html)。同理还有[![能量接口 (Energy Interface)](https://i.mcmod.cn/item/icon/32x32/17/177475.png)](https://www.mcmod.cn/item/177475.html)[能量接口](https://www.mcmod.cn/item/177475.html)和[![流体接口 (Fluid Interface)](https://i.mcmod.cn/item/icon/32x32/17/177485.png)](https://www.mcmod.cn/item/177485.html)[流体接口](https://www.mcmod.cn/item/177485.html)，以及他们的输入器、输出器——[物品输入口](https://www.mcmod.cn/item/177481.html)和[物品输出口](https://www.mcmod.cn/item/177482.html)。

如果要传输红石信号，只需要[![红石输出 (Redstone Writer)](https://i.mcmod.cn/item/icon/32x32/6/63151.png)](https://www.mcmod.cn/item/63151.html)[红石输出](https://www.mcmod.cn/item/63151.html)和[![红石读取器 (Redstone Reader)](https://i.mcmod.cn/item/icon/32x32/6/63146.png)](https://www.mcmod.cn/item/63146.html)[红石读取器](https://www.mcmod.cn/item/63146.html)。

除此之外，你还需要在所有的接口和设备中使用[![变量卡 (Variable Card)](https://i.mcmod.cn/item/icon/32x32/6/63181.png)](https://www.mcmod.cn/item/63181.html)[变量卡](https://www.mcmod.cn/item/63181.html)。

#### 网络和频道

在开始介绍物流前，还需要介绍一个概念就是【网络】和【频道】。

和AE2类似，使用逻辑线缆相连的，所有ID模组中的读取器、输出器、接口，以及它们直接连接的机器，合在一起为一个**<u>网络</u>**。

网络内部拥有**<u>频道</u>**，所有的输出器、输入器和接口都拥有一个**<u>频道</u>**，只有同一个网络内的，相同**<u>频道</u>**的输出器、输入器和接口才会互相连接。（特别的，对于物品而言，即使是不同频道的物品接口也会互通，对于容易误串的地方使用输入或输出接口、或严格筛选物品！）

另外，每个频道至少需要一个**<u>接口</u>**，单纯放置输出器和输入器是不会起效果的，因为ID物流的本质是将物品从输入器中提取到接口对应的容器中，再输出到输出器。

#### 物流网络

现在你可以放置一个简单的物流网络做一个测试：

![](/ID1.png)

右侧放置的是物品输出口。不过它并没有起到效果，因为我还没有配置这些接口。

![](/ID2.png)

右键输出口，我们可以看到这样一个配置面板。你需要将配置好的变量卡放在里面作为筛选条件。

![](/ID3.png)

如果你没有很复杂的操作，只需要将空变量卡放在第一行即可，或者是接受类型为布尔的那一行（你可以将鼠标悬浮在行首的图标上查看需要放置的变量卡类型，空变量卡为布尔）。

如果你不需要额外的设置，这个时候简单的物流传输就已经完成了。他会以默认64物品/tick的速度传输物品，咻！

## 第三节 简单设置

不过如果只是单纯的将变量卡放在第一行，不进行任何额外的操作，那么只是一个毫无筛选的快速管道而已——虽然已经可以完成绝大部分的操作了。

接下来我要简单介绍一些常用的配置。

![](/ID4.png)

在放置变量卡时，不知道你有没有注意到这里的加号，点开他，里面别有洞天！

![](/ID5.png)![](/ID6.png)

你可以通过上面的箭头进行页面切换。通常来说，我们需要修改的配置只有【频道】和【物品传输速率】。

频道在上面已经介绍过了，通过修改频道就可以指定物品从哪来到哪去——注意，物品接口也要对应的修改频道，而物品接口修改频道时一定要点【保存】！

物品传输速率，通常而言就是多多益善了，最高可以填2147483647！不过很多时候，机器本身也有输入输出的上限。

通过加号键的配置，你已经可以完成80%以上的自动化和物流操作了，而且速度超快，远超其他任何一种管道。但是目前你只能通过频道进行简单的筛选，如果你需要更高的自由度和更智能配置，请继续向下看。

## 第四节 变量卡浅谈

如果要用好变量卡，还需要六个设备：

[![变量卡箱 (Variable Store)](https://i.mcmod.cn/item/icon/32x32/6/63156.png)](https://www.mcmod.cn/item/63156.html)[变量卡箱](https://www.mcmod.cn/item/63156.html)，[![逻辑编程器 (Logic Programmer)](https://i.mcmod.cn/item/icon/32x32/6/63157.png)](https://www.mcmod.cn/item/63157.html)[逻辑编程器](https://www.mcmod.cn/item/63157.html)（或[![便携式逻辑编辑器 (Portable Logic Programmer)](https://i.mcmod.cn/item/icon/32x32/6/63188.png)](https://www.mcmod.cn/item/63188.html)[便携式逻辑编辑器](https://www.mcmod.cn/item/63188.html))，[![代理器 (Proxy)](https://i.mcmod.cn/item/icon/32x32/6/63162.png)](https://www.mcmod.cn/item/63162.html)[代理器](https://www.mcmod.cn/item/63162.html)，[![复制器 (Materializer)](https://i.mcmod.cn/item/icon/32x32/6/63163.png)](https://www.mcmod.cn/item/63163.html)[固值器](https://www.mcmod.cn/item/63163.html)，[![延迟器 (Delayer)](https://i.mcmod.cn/item/icon/32x32/6/63179.png)](https://www.mcmod.cn/item/63179.html)[延迟器](https://www.mcmod.cn/item/63179.html)，和查看变量值的[![显示器 (Display Panel)](https://i.mcmod.cn/item/icon/32x32/6/63154.png)](https://www.mcmod.cn/item/63154.html)[显示器](https://www.mcmod.cn/item/63154.html)

在本章中，我们只涉及逻辑编程器和变量卡箱。

![ID7](/ID7.png)

打开逻辑编程器可以看出，变量卡拥有非常非常多的类型，在本章中，只简单介绍***整形***、***对应物品***、***流体***和***列表***四种类型。

在最上面可以输入文字进行筛选，绿色的格子可以放入变量卡进行筛选（高级功能，这里不介绍），红色部分就是列出的类型表，点击便可以选中类型，而紫色格子用于放置变量卡。

![image-20200528225524430](/ID8.png)

![image-20200528225559430](/ID9.png)

![image-20200528225626414](/ID10.png)

![image-20200528225702878](/ID11.png)

以上就是一些最简单的配置方式：输入数字、或是将物品放入格子内，即可完成变量卡的配置。如果是列表型，需要选择列表内要添加的物品类型，放置完成后点一下旁边的加号，才能将物品加入列表。请保证列表内是同一个类型的参数，以免发生不必要的错误。

![image-20200528225921478](/ID12.png)

配置完成后，你就可以将对应的变量卡放入输出口中进行更高级的筛选了。黄色圈出来的是变量卡对应的值，可以帮助你确认变量卡是否正确。现在这个箱子只会接受物品接口和物品输出口了。你也可以将模式改为黑名单，或是匹配nbt和数量等等，还有很多功能可以进行探索。

更高级的筛选和自动化相关的部分我会在论集成动力下中进行介绍，有兴趣的话可以继续查看。