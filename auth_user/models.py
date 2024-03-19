from django.db import models
from django.contrib.auth.models import AbstractUser, BaseUserManager

class User(AbstractUser):
    class Role(models.TextChoices):
        DEFAULT_USER = "DEFAULT_USER", 'Default User'
        SECURITY = "SECURITY", 'Security'
        RECEPTIONIST = "RECEPTIONST", 'Receptionist'
        WAREHOUSE_OPERATIVE = "WAREHOUSE_OPERATIVE", 'Warehouse Operative'
        WAREHOUSE_ADMIN = "WAREHOUSE_ADMIN", 'Warehouse Admin'
        WAREHOUSE_TEAM_LEADER = "WAREHOUSE_TEAM_LEADER", 'Warehouse Team Leader'
        WAREHOUSE_MANAGER = "WAREHOUSE_MANAGER", 'Warehouse Manager'
        INVENTORY_ADMIN = "INVENTORY_ADMIN", 'Inventory Admin'
        INVENTORY_TEAM_LEADER = "INVENTORY_TEAM_LEADER", 'Inventory Team Leader'
        INVENTORY_MANAGER = "INVENTORY_MANAGER", 'Inventory Manager'
        OPERATIONAL_MANAGER = "OPERATIONAL_MANAGER", 'Operational Manager'
    
    base_role = Role.DEFAULT_USER
    
    role = models.CharField(max_length=50, choices=Role.choices)
    
    def save(self, *args, **kwargs):
        if not self.pk:
            self.role = self.base_role
            return super().save(*args, **kwargs)
        
class SecurityManager(BaseUserManager):
    def get_queryset(self, *args, **kwargs):
        results = super().get_queryset(*args, **kwargs)
        return results.filter(role=User.Role.SECURITY)
        
class Security(User):
    
    base_role = User.Role.SECURITY
    
    class Meta:
        proxy = True
        
    def welcome(self):
        return "Warehouse Security Gate Only"
        
