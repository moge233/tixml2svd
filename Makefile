
DEVICE=CC3220SF
DEVICE_SVD=$(DEVICE).svd

PY=python3


all:
	make build


.PHONY: clean
clean:
	rm -rfv $(DEVICE_SVD) $(DEVICE)


.PHONY: build
build:
	$(PY) tixml2svd.py ./targetdb/devices/$(DEVICE).xml $(DEVICE_SVD)
