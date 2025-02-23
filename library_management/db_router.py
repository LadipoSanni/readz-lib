class LibraryRouter:
    """
    Routes database operations to separate databases for frontend and backend services.
    """

    def db_for_read(self, model, **hints):
        """Directs frontend_api models to the default DB and backend_api models to backend DB."""
        if model._meta.app_label == 'frontend_api':
            return 'default'
        elif model._meta.app_label == 'backend_api':
            return 'backend'
        return None

    def db_for_write(self, model, **hints):
        """Directs writes to the correct database."""
        return self.db_for_read(model, **hints)

    def allow_relation(self, obj1, obj2, **hints):
        """Allows relations within the same database only."""
        if obj1._state.db == obj2._state.db:
            return True
        return False

    def allow_migrate(self, db, app_label, model_name=None, **hints):
        """Ensures migrations apply to the correct database."""
        if app_label == 'frontend_api':
            return db == 'default'
        elif app_label == 'backend_api':
            return db == 'backend'
        return None
