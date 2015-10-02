
var typeOf = function(item) {
    'use strict';
    if (item === null) {
        return 'null';  
    }
    if (typeof(item) === 'string')
        return 'string';
    if (item.nodeName) {
        if (item.nodeType === 1) {
            return 'element';
        }
        if (item.nodeType === 3) {
            return (/\S/).test(item.nodeValue) ? 'textnode' : 'whitespace';
        }
    } else if (typeof item.length === 'number') {
        if (item.callee) {
            return 'arguments';
        }
        if ('item' in item) {
            return 'collection';
        }
    }
    return typeof item;
};

//get element from id, class or jquery object
var normalizeElement = function(element) {
    var type = typeOf(element);
    if(type === 'element')
        return element;
    if(element instanceof jQuery)
        return element[0];
    if(type === 'string') {
        return document.querySelector(element) || document.querySelector('#' + element) || document.querySelector('.' + element);
    }
};

var Popover = (function() {
    function Popover(elm, trigger, options) {
        var self = this;
        this.options = {
            multiTriggers: false
        };
        _.extend(this.options, options);
        if(this.options.multiTriggers) {
            this.trigger = $(trigger);
        }
        else {
            this.trigger = $(normalizeElement(trigger));

        }

        this.dialog = $(normalizeElement(elm));
        this.trigger.on('click', function() {
            self.open();
        });
        this.state = 'closed';
    }

    Popover.prototype.open = function() {
        var self = this;
        if(this.state === 'open') {
            self.close();

            return;
        }
        var dialog = this.dialog.position({
            my: 'left top',
            at: 'left bottom+8px',
            of:  this.trigger,
            collision: 'fit',
            offset: "30px 30px"
        }).addClass('open');
        this.closeOutside();
        this.state = 'open';
    }

    Popover.prototype.closeOutside = function() {
        var self = this;
        this.closeEvent = function(e) {
            if(self.dialog.hasClass('open')
                && !$(e.target).is('.popOver')
                && !$(e.target).closest('.popOver').length
                && !$(e.target).is(self.trigger)
            ) {
                e.preventDefault();
                self.close();
            }
        }
        $('body').on('click', function(e) {
            self.closeEvent(e);
        });
    }

    Popover.prototype.close = function() {
        var self = this;
        this.dialog.removeClass('open');
        this.dialog.attr('style', '');
        setTimeout(function() {
            $('body').off('click', self.closeEvent);
        });
        self.state = 'closed';
    }
    return Popover;

})();