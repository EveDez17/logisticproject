from django.db import models
from django.contrib.auth.models import AbstractUser, BaseUserManager


class User(AbstractUser):
    class Role(models.TextChoices):
        DEFAULT_USER = "DEFAULT_USER", "Default User"
        SECURITY = "SECURITY", "Security"
        RECEPTIONIST = "RECEPTIONST", "Receptionist"
        WAREHOUSE_OPERATIVE = "WAREHOUSE_OPERATIVE", "Warehouse Operative"
        WAREHOUSE_ADMIN = "WAREHOUSE_ADMIN", "Warehouse Admin"
        WAREHOUSE_TEAM_LEADER = "WAREHOUSE_TEAM_LEADER", "Warehouse Team Leader"
        WAREHOUSE_MANAGER = "WAREHOUSE_MANAGER", "Warehouse Manager"
        INVENTORY_ADMIN = "INVENTORY_ADMIN", "Inventory Admin"
        INVENTORY_TEAM_LEADER = "INVENTORY_TEAM_LEADER", "Inventory Team Leader"
        INVENTORY_MANAGER = "INVENTORY_MANAGER", "Inventory Manager"
        OPERATIONAL_MANAGER = "OPERATIONAL_MANAGER", "Operational Manager"

    base_role = Role.DEFAULT_USER

    role = models.CharField(max_length=50, choices=Role.choices)

    def save(self, *args, **kwargs):
        if not self.pk and self.role == User.Role.DEFAULT_USER:
            self.role = self.base_role
        super().save(*args, **kwargs)


class SecurityManager(BaseUserManager):
    def get_queryset(self, *args, **kwargs):
        results = super().get_queryset(*args, **kwargs)
        return results.filter(role=User.Role.SECURITY)


class Security(User):

    base_role = User.Role.SECURITY

    security = SecurityManager()

    class Meta:
        proxy = True

    def welcome(self):
        return "Warehouse Security Gate Only"


class ReceptionistManager(BaseUserManager):
    def get_queryset(self, *args, **kwargs):
        results = super().get_queryset(*args, **kwargs)
        return results.filter(role=User.Role.RECEPTIONIST)


class Receptionist(User):

    base_role = User.Role.RECEPTIONIST

    reception = ReceptionistManager()

    class Meta:
        proxy = True

    def welcome(self):
        return "Reception Staff Only"


class WarehouseOperativeManager(BaseUserManager):
    def get_queryset(self, *args, **kwargs):
        results = super().get_queryset(*args, **kwargs)
        return results.filter(role=User.Role.WAREHOUSE_OPERATIVE)


class WarehouseOperative(User):

    base_role = User.Role.WAREHOUSE_OPERATIVE

    w_operative = WarehouseOperativeManager()

    class Meta:
        proxy = True

    def welcome(self):
        return "Warehouse Operatives Only"


class WarehouseAdminManager(BaseUserManager):
    def get_queryset(self, *args, **kwargs):
        results = super().get_queryset(*args, **kwargs)
        return results.filter(role=User.Role.WAREHOUSE_ADMIN)


class WarehouseAdmin(User):

    base_role = User.Role.WAREHOUSE_ADMIN

    w_admin = WarehouseAdminManager()

    class Meta:
        proxy = True

    def welcome(self):
        return "Warehouse Admins Only"


class WarehouseTeamLeaderManager(BaseUserManager):
    def get_queryset(self, *args, **kwargs):
        results = super().get_queryset(*args, **kwargs)
        return results.filter(role=User.Role.WAREHOUSE_TEAM_LEADER)


class WarehouseTeamLeader(User):

    base_role = User.Role.WAREHOUSE_TEAM_LEADER

    warehouse_tl = WarehouseTeamLeaderManager()

    class Meta:
        proxy = True

    def welcome(self):
        return "Warehouse Team Leaders Only"


class WarehouseManagerManager(BaseUserManager):
    def get_queryset(self, *args, **kwargs):
        results = super().get_queryset(*args, **kwargs)
        return results.filter(role=User.Role.WAREHOUSE_MANAGER)


class WarehouseManager(User):

    base_role = User.Role.WAREHOUSE_MANAGER

    w_manager = WarehouseManagerManager()

    class Meta:
        proxy = True

    def welcome(self):
        return "Warehouse Managers Only"


class InventoryAdminManager(BaseUserManager):
    def get_queryset(self, *args, **kwargs):
        results = super().get_queryset(*args, **kwargs)
        return results.filter(role=User.Role.INVENTORY_ADMIN)


class InventoryAdmin(User):

    base_role = User.Role.INVENTORY_ADMIN

    inv_admin = InventoryAdminManager()

    class Meta:
        proxy = True

    def welcome(self):
        return "Inventory Admins Only"


class InventoryTeamLeaderManager(BaseUserManager):
    def get_queryset(self, *args, **kwargs):
        results = super().get_queryset(*args, **kwargs)
        return results.filter(role=User.Role.INVENTORY_TEAM_LEADER)


class InventoryTeamLeader(User):

    base_role = User.Role.INVENTORY_TEAM_LEADER

    inv_tl = InventoryTeamLeaderManager()

    class Meta:
        proxy = True

    def welcome(self):
        return "Inventory Team Leaders Only"


class InventoryManagerManager(BaseUserManager):
    def get_queryset(self, *args, **kwargs):
        results = super().get_queryset(*args, **kwargs)
        return results.filter(role=User.Role.INVENTORY_MANAGER)


class InventoryManager(User):

    base_role = User.Role.INVENTORY_MANAGER

    inv_manager = InventoryManagerManager()

    class Meta:
        proxy = True

    def welcome(self):
        return "Inventory Managers Only"


class OperationalManagerManager(BaseUserManager):
    def get_queryset(self, *args, **kwargs):
        results = super().get_queryset(*args, **kwargs)
        return results.filter(role=User.Role.OPERATIONAL_MANAGER)


class OperationalManager(User):

    base_role = User.Role.OPERATIONAL_MANAGER

    ops_manager = OperationalManagerManager()

    class Meta:
        proxy = True

    def welcome(self):
        return "Operational Manager Only"
