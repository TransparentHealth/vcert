from django.contrib import admin
from mptt.admin import MPTTModelAdmin
from models import ( EndpointCertificate, TrustAnchorCertificate,
                    CertificateRevocationList, AnchorCertificateRevocationList)



class TreeViewAnchorCertificate(TrustAnchorCertificate):
    class Meta:
        proxy = True
        verbose_name = "Tree View of Anchor"


class EndpointCertificateAdmin(admin.ModelAdmin):
    
    list_display = ('common_name', 'trust_anchor','status','verified',
                    'serial_number', 'organization', 'creation_date', 
                    'expiration_date')
    
    search_fields = ('common_name','status', 'verified','serial_number',
                     'organization', 'creation_date', 'expiration_date')
    
admin.site.register(EndpointCertificate, EndpointCertificateAdmin)


class TrustAnchorCertificateAdmin(admin.ModelAdmin):
    
    #def queryset(self, request):
    #    return self.model.objects.filter(user = request.user)

    list_display = ('domain','parent', 'status', 'verified', 'serial_number',
                    'organization', 'creation_date', 'expiration_date')
    
    search_fields = ( 'common_name', 'domain', 'email',  'parent__common_name', 'status','verified', 'serial_number',
                     'organization', 'creation_date', 'expiration_date')

    
admin.site.register(TrustAnchorCertificate, TrustAnchorCertificateAdmin)





class TreeViewAdmin(MPTTModelAdmin):
                   
    search_fields = ('common_name','parent',)
    
    #def queryset(self, request):
    #    return self.model.objects.filter(user = request.user)
    
admin.site.register(TreeViewAnchorCertificate, TreeViewAdmin)



class CertificateRevocationListAdmin(admin.ModelAdmin):
    
    list_display = ( 'url', 'local_path', 'creation_date', 'creation_datetime')
    
    search_fields =('url', 'local_path','creation_date', 'creation_datetime')
    
admin.site.register(CertificateRevocationList, CertificateRevocationListAdmin)


class AnchorCertificateRevocationListAdmin(admin.ModelAdmin):
    
    list_display = ('trust_anchor','url', 'local_path', 'creation_date', 
                    'creation_datetime')
    
    search_fields =('trust_anchor','url', 'local_path', 'creation_date', 
                    'creation_datetime')
    
admin.site.register(AnchorCertificateRevocationList, AnchorCertificateRevocationListAdmin)

