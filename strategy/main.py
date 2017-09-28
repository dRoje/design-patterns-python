import duck
import flyBehavior

mallardDuck = duck.MallardDuck()
mallardDuck.performFly()
mallardDuck.performQuack()

print

modelDuck = duck.ModelDuck()
modelDuck.performFly()
modelDuck.setFlyBehavior(flyBehavior.FlyRocketPowered())
modelDuck.performFly()