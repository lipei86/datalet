# 简介
datalet是一个用于数据分析的辅助工具集。datalet的目标不是数据分析，而是提供数据分析之外的辅助工具。比如提供文件、数据库的IO抽象；可以使用Python连接Mondrian的Gateway等等。

建立datalet的意图是减少数据分析工作中那些不必要浪费时间的工作。让数据分析师将更多的时间用于数据分析上。


# 模块[datalet.data]
datalet.data的数据结构模仿dotnet的DataSet。包中主要的对象是DataTable，它记录了表格的行和列，并且可与其他通用数据结构（比如pandas的DataFrame）进行转换。

与dotnet的DataSet的区别：

datalet.data与dotnet的DataSet不同的是dotnet的DataSet是write-schema，即在添加数据时进行模式验证，而datalet.data借鉴了hive的数据存储方式，采用的是read-schema，个人认为这种模式更适合数据分析工作。


与pandas.DataFrame的区别：

pandas.DataFrame是基于numpy的，每一列的值的数据类型都必须是一致。所以就限制了数据的格式不利于数据的加载。

假如列是float类型，但存在个空值，这个空值会采用np.nan表示，而不能使用None表示。

如果使用to_dict将DataFrame转换为dict，再使用SqlAlchemy记载到数据库的话，会报错提示np.nan超出数值型范围。

对于此种情况，datalet.data就可以很容易的处理，因为他是read-schema，不在乎内部的实际存储格式，对于空值它将采用Null来表示，或者采用指定的值表示。

其实datalet.data与pandas.DataFrame的目的是不同的。DataFrame的目的是分析数据，datalet.data的目的是数据的内存载体，用于做ELT比较合适。


# 模块[datalet.storage]
storage表示一个数据载体。每个载体都可以将数据读出到内存，或将内存中数据写入载体。

支持的载体类型有CSV文件、EML文件、Excel文件、数据库表。

有针对各个载体类型的类，还有个Facade类，用于将所有的storage都汇集在这里。

# 模块[datalet.olap]
采用Java中大名鼎鼎的Mondrian作为OLAP引擎。可以支持标准Schema定义、MDX查询。

# 模块[datalet.logging]
在使用Logger时，会自动判断工作文件夹下是否存在日志配置文件，如果没有则使用默认的配置文件。

# 模块[datalet.ml]
为机器学习提供辅助

# RoadMap
1. 支持关系型数据库的分区存储


# 用法示例
1. 合并多个文件的数据后保存到指定文件

2. 下载数据库表的数据到文件

3. 获取文件的某一列

4. 对某个数据库执行MDX查询
