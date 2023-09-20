eqPath = 'ECS/EVV/Packaging/Line 1/Filler'
equip = system.ecs.equipment.getEquipment(eqPath)

print equip

#print system.ecs.oee.multiply(2, 3)
#
#d = system.ecs.cache.getCacheStats()
#print d






eqPath = 'Mizkan/Owensboro/Packaging/Line 1'
#equip = system.ecs.equipment.getEquipment(eqPath)
#
#print equip

#print system.ecs.oee.multiply(2, 3)
#
d = system.ecs.cache.getCacheStats()
print d

endDate = system.date.now()
startDate = system.date.addDays(endDate, -1)

evts = system.ecs.dt.getStateEvents(eqPath, startDate.getTime(), endDate.getTime())
print evts