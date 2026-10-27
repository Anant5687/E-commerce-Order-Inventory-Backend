E-commerce-order-inventory-backend/
├── app/
│   ├── main.py                    # app factory, lifespan, middleware, routers
│   ├── core/
│   │   ├── config.py              # Settings (env based)
│   │   ├── security.py            # JWT create/verify, hash/verify password
│   │   ├── logging.py
│   │   ├── exceptions.py          # AppException, NotFound, Conflict, etc.
│   │   ├── error_handlers.py      # global exception handlers
│   │   └── constants.py           # enums: Role, OrderStatus, PaymentStatus
│   ├── db/
│   │   ├── base.py                # DeclarativeBase + import all models
│   │   ├── session.py             # async engine, sessionmaker, get_db
│   │   ├── mixins.py              # TimestampMixin, SoftDeleteMixin
│   │   └── uow.py                 # Unit of Work (transaction boundary)
│   ├── models/
│   │   ├── user.py  address.py  refresh_token.py
│   │   ├── category.py  product.py  product_image.py
│   │   ├── inventory.py  inventory_movement.py
│   │   ├── cart.py  cart_item.py
│   │   ├── order.py  order_item.py  payment.py
│   │   ├── idempotency_key.py  outbox_event.py  audit_log.py
│   ├── schemas/                   # Pydantic: Create / Update / Read / filters
│   │   ├── common.py              # Pagination, PageResponse, Msg
│   │   ├── auth.py user.py address.py category.py product.py
│   │   ├── inventory.py cart.py order.py payment.py report.py
│   ├── repositories/              # ONLY DB queries, no business logic
│   │   ├── base.py  user.py  product.py  inventory.py
│   │   ├── cart.py  order.py  payment.py  outbox.py ...
│   ├── services/                  # business logic + transaction orchestration
│   │   ├── auth_service.py  user_service.py  product_service.py
│   │   ├── inventory_service.py  cart_service.py  order_service.py
│   │   ├── payment_service.py  invoice_service.py  report_service.py
│   ├── integrations/              # external world (async)
│   │   ├── payment_gateway.py     # httpx client to mock gateway
│   │   ├── email_client.py
│   │   └── cache.py               # redis wrapper
│   ├── blocking/                  # sync functions that run in to_thread
│   │   ├── pdf_invoice.py  csv_excel.py  image_ops.py  hashing.py
│   ├── workers/
│   │   ├── settings.py            # ARQ WorkerSettings
│   │   └── tasks.py               # send_email, process_outbox, expire_orders
│   ├── middleware/
│   │   ├── request_id.py  logging_mw.py  rate_limit.py
│   └── api/
│       ├── deps.py                # get_db, get_current_user, require_role
│       └── v1/
│           ├── router.py
│           └── endpoints/
│               auth.py users.py addresses.py categories.py products.py
│               inventory.py cart.py orders.py payments.py reports.py health.py
├── alembic/  (+ alembic.ini)
├── tests/
│   ├── conftest.py  unit/  integration/
├── docker-compose.yml   # api, postgres, redis, worker
├── Dockerfile
├── .env.example
├── Makefile
└── pyproject.toml
