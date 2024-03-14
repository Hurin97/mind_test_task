from pyspark.sql import SparkSession, DataFrame


spark = SparkSession.builder.getOrCreate()

product_catalog = spark.createDataFrame([
    (1, 'chocolate'),
    (2, 'cheese'),
    (3, 'chicken legs'),
    (4, 'bread'),
    (5, 'lemonade'),
    (6, 'milk')],
    ['id', 'product']
)
category_catalog = spark.createDataFrame([
    (1, 'meat'),
    (2, 'beverages'),
    (3, 'dairy')],
    ['id', 'category']
)
product_to_category_ratio = spark.createDataFrame([
    (2, 3),
    (3, 1),
    (5, 2),
    (6, 2),
    (6, 3)],
    ['product_id','category_id']
    )

pivot_table = product_catalog.join(product_to_category_ratio,
    product_catalog.id == product_to_category_ratio.product_id, how='left').join(category_catalog,
    product_to_category_ratio.category_id == category_catalog.id, how='left').select(['product', 'category'])

pivot_table.orderBy('product', 'category').show()