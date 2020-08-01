@admin.register(Product)
class ProductAdmin(admin.ModelAdmin):
    def formfield_for_foreignkey(self, db_field, request, **kwargs):
        if db_field.name == 'subcat':
            kwargs["queryset"] = Subcat.objects.filter(category_id = 2)
        return super().formfield_for_foreignkey(db_field, request, **kwargs)
