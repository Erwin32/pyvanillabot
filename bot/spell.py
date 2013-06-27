class SpellList(list):


class Spell(object):

    def __init__(self, name, weight):

        self.Weight = weight
        self.Name = name

        self.Cost = self.get_spell_cost()
        self.CastTime = self.get_spell_cast_time()
        self.OnCooldown = self.get_cooldown_state()

    def get_spell_cost(self):
        ProcessManager.Injector.Lua_DoString(string.Format("name, rank, icon, cost, isFunnel, powerType, castTime, minRange, maxRange = GetSpellInfo(\"{0}\");", Name));
        cost = ProcessManager.Injector.Lua_GetLocalizedText(3);
        return int(cost)

    def get_spell_cast_time(self):
        ProcessManager.Injector.Lua_DoString(string.Format("name, rank, icon, cost, isFunnel, powerType, castTime, minRange, maxRange = GetSpellInfo(\"{0}\");", Name));
        cast_time = ProcessManager.Injector.Lua_GetLocalizedText(6);
        return int(cast_time)

    def get_cooldown_state(self):
        ProcessManager.Injector.Lua_DoString(string.Format("start, duration, enabled = GetSpellCooldown(\"{0}\");", Name));
        duration = ProcessManager.Injector.Lua_GetLocalizedText(1);

        return duration
