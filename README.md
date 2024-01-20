## What this Repo is for ?
It contains source code for tutorial published at
https://medium.com/@mansha99/microservices-in-python-django-rabbitmq-and-pika-fe1adb0c6a1a

## rabbitMq 学习笔记
- 异步调用优势&问题
  - 耦合度低，可扩展性好
  - 故障隔离
  - 流量削峰填谷
  - 时效性差
  - 不确定下游是否成功
  - 业务安全依赖于消息代理（broker）的可靠性
- rabbitMq由 producer、exchange（交换器，：路由）、queue（队列）、consumer组成，其中，exchange和queue需要绑定
- producer不直连queue，而是exchange的好处在于：
  - 拥有较为灵活的配对方式：直连、扇出、匹配
  - 单生产者多队列，多生产者单队列，多生产者多队列
  - 异步发送，不用等待消息进入队列
  - 消息过滤逻辑处理
  - 扩展性好
  - 消息持久化
- virtual host的作用：帮助进行数据、权限、故障、资源分配的隔离
- work模型：
  - 多个消费者绑定一个队列，解决消息堆积的问题
  - 消息只会被消费1次
  - 可以通过prefetch参数来平衡不同性能的消费者，能者多劳
- 交换机：实际应用较多
  - fanout：